"""
MTGA Card Sync — Combined Collection & Deck Tracker
====================================================
One script that does everything:

1. Instantly scans the existing log for all deck edits and collection dumps
2. Resolves card IDs to names via the local MTGA SQLite database
3. Saves everything to persistent master files
4. Then watches the log live for new deck edits and collection data

Usage:
    python mtga_card_sync.py          # Scan + watch mode (default)
    python mtga_card_sync.py --scan   # Scan only, don't watch
    python mtga_card_sync.py --watch  # Watch only, skip initial scan

Output files:
    deck_data_raw.json       - Raw deck dumps with card IDs and quantities
    all_cards_resolved.json  - Master card database with names, types, mana costs
    card_inventory.txt       - Human-readable card list sorted by type

The more decks you open/edit in Arena, the more cards get captured.
If the full collection dump fires on login (GetPlayerCardsV3), that
gives us everything at once.
"""

import json
import os
import re
import sys
import time
import sqlite3
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.expandvars(
    r"%APPDATA%\..\LocalLow\Wizards Of The Coast\MTGA\Player.log"
)
CARD_DB_DIR = r"C:\Program Files (x86)\Steam\steamapps\common\MTGA\MTGA_Data\Downloads\Raw"

# Output files
RAW_FILE = os.path.join(SCRIPT_DIR, "deck_data_raw.json")
RESOLVED_FILE = os.path.join(SCRIPT_DIR, "all_cards_resolved.json")
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "card_inventory.txt")
COLLECTION_FILE = os.path.join(SCRIPT_DIR, "my_collection.json")


# ─── Card Database ───────────────────────────────────────────────────────────


def find_card_database():
    """Find the MTGA SQLite card database file."""
    for f in os.listdir(CARD_DB_DIR):
        if "CardDatabase" in f and f.endswith(".mtga"):
            return os.path.join(CARD_DB_DIR, f)
    return None


def resolve_card_ids(card_ids):
    """Resolve card IDs to names/types/mana using the MTGA SQLite database."""
    db_path = find_card_database()
    if not db_path:
        print("  ERROR: Could not find MTGA card database")
        return {}

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Process in batches to avoid SQLite variable limits
    card_list = list(card_ids)
    card_db = {}
    batch_size = 500
    rarity_map = {0: "common", 1: "uncommon", 2: "rare", 3: "mythic"}

    for i in range(0, len(card_list), batch_size):
        batch = card_list[i : i + batch_size]
        placeholders = ",".join(["?" for _ in batch])
        cursor.execute(
            f"""
            SELECT c.GrpId, l.Loc, t.Loc, s.Loc,
                   c.OldSchoolManaText, c.Power, c.Toughness, c.Rarity, c.Colors
            FROM Cards c
            LEFT JOIN Localizations_enUS l ON c.TitleId = l.LocId
            LEFT JOIN Localizations_enUS t ON c.TypeTextId = t.LocId
            LEFT JOIN Localizations_enUS s ON c.SubtypeTextId = s.LocId
            WHERE c.GrpId IN ({placeholders})
            """,
            batch,
        )
        for row in cursor.fetchall():
            grp_id, name, type_line, subtype, mana, power, tough, rarity, colors = row
            card_db[grp_id] = {
                "name": name or f"Unknown#{grp_id}",
                "type": type_line or "",
                "subtype": subtype or "",
                "mana": mana or "",
                "power": power or "",
                "toughness": tough or "",
                "rarity": rarity_map.get(rarity, "unknown"),
                "colors": colors or "",
            }

    conn.close()
    return card_db


# ─── Log Scanning ────────────────────────────────────────────────────────────


def extract_decks_from_log():
    """Extract all deck edit events from the MTGA Player.log."""
    if not os.path.exists(LOG_PATH):
        print(f"  Player.log not found at {LOG_PATH}")
        return []

    decks = []
    with open(LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f):
            if "DeckUpsertDeckV2" not in line:
                continue
            if "request" not in line or "==>" not in line:
                continue
            deck = _parse_deck_line(line, i)
            if deck:
                decks.append(deck)

    return decks


def extract_collection_from_log():
    """Search the existing log for a full collection dump (GetPlayerCardsV3)."""
    if not os.path.exists(LOG_PATH):
        return None

    with open(LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Method 1: GetPlayerCardsV3 response
    if "GetPlayerCardsV3" in content:
        match = re.search(r"GetPlayerCardsV3.*?(\{.*\})", content, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(1))
                card_data = _filter_collection(data)
                if card_data and len(card_data) > 50:
                    return card_data
            except json.JSONDecodeError:
                pass

    # Method 2: Large JSON with numeric keys (card ID -> count)
    for line in content.split("\n"):
        line = line.strip()
        if not line.startswith("{"):
            continue
        card_pattern = re.findall(r'"(\d{4,6})"\s*:\s*(\d+)', line)
        if len(card_pattern) > 200:  # Full collection has hundreds of entries
            try:
                data = json.loads(line)
                card_data = _filter_collection(data)
                if card_data and len(card_data) > 200:
                    return card_data
            except json.JSONDecodeError:
                continue

    return None


def _parse_deck_line(line, line_num=0):
    """Parse a single DeckUpsertDeckV2 log line into deck data."""
    try:
        json_start = line.index("{")
        outer = json.loads(line[json_start:])
        request = json.loads(outer["request"])
        name = request.get("Summary", {}).get("Name", "Unknown")
        deck = request.get("Deck", {})
        main_deck = deck.get("MainDeck", [])
        sideboard = deck.get("Sideboard", [])
        companions = deck.get("Companions", [])

        if main_deck:
            total = sum(e.get("quantity", 0) for e in main_deck)
            return {
                "name": name,
                "format": "Historic",
                "main_deck": main_deck,
                "sideboard": sideboard,
                "companions": companions,
                "total_cards": total,
                "log_line": line_num,
            }
    except (json.JSONDecodeError, ValueError, KeyError):
        pass
    return None


def _filter_collection(data):
    """Filter a JSON object to only card ID -> count pairs."""
    if not isinstance(data, dict):
        return None
    card_data = {}
    for k, v in data.items():
        if k.isdigit() and isinstance(v, int) and v > 0:
            card_data[int(k)] = v
    return card_data if len(card_data) > 0 else None


# ─── Data Persistence ────────────────────────────────────────────────────────


def load_existing_raw():
    """Load previously saved raw deck data."""
    if os.path.exists(RAW_FILE):
        with open(RAW_FILE, "r") as f:
            return json.load(f)
    return {"decks": [], "unique_card_ids": []}


def merge_decks(new_decks, old_data):
    """Merge new deck data with existing, keeping decks not in the new log."""
    all_decks = list(new_decks)
    new_names = {d["name"] for d in new_decks}

    kept = 0
    for deck in old_data.get("decks", []):
        if deck.get("name") not in new_names:
            all_decks.append(deck)
            kept += 1

    if kept:
        print(f"  Kept {kept} decks from previous saves")

    return all_decks


def collect_all_card_ids(decks, collection=None):
    """Gather all unique card IDs from decks and optional collection."""
    ids = set()
    for deck in decks:
        for entry in deck.get("main_deck", []):
            ids.add(entry["cardId"])
        for entry in deck.get("sideboard", []):
            ids.add(entry["cardId"])
        for entry in deck.get("companions", []):
            ids.add(entry["cardId"])

    if collection:
        ids.update(collection.keys())

    return ids


def save_raw(all_decks, all_ids):
    """Save raw deck data."""
    output = {
        "decks": all_decks,
        "unique_card_ids": sorted(list(all_ids)),
    }
    with open(RAW_FILE, "w") as f:
        json.dump(output, f, indent=2)


def save_collection_data(collection, card_db):
    """Save the full collection dump if we got one."""
    output = {}
    for cid, count in collection.items():
        info = card_db.get(cid, {})
        output[str(cid)] = {
            "name": info.get("name", f"Unknown#{cid}"),
            "count": count,
        }
    with open(COLLECTION_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Full collection saved: {len(output)} cards -> {COLLECTION_FILE}")


def build_master_file(all_decks, card_db, collection=None):
    """Build the master resolved card file."""
    # Load existing to preserve data
    existing = {}
    if os.path.exists(RESOLVED_FILE):
        with open(RESOLVED_FILE, "r", encoding="utf-8") as f:
            old = json.load(f)
            existing = old.get("all_cards", {})

    # Build deck summaries
    deck_summaries = {}
    for deck in all_decks:
        name = deck["name"]
        cards = []
        for entry in deck.get("main_deck", []):
            cid = entry["cardId"]
            qty = entry["quantity"]
            info = card_db.get(cid, {})
            cards.append({
                "id": cid,
                "qty": qty,
                "name": info.get("name", f"Unknown#{cid}"),
            })
        deck_summaries[name] = cards

    # Build master card list
    all_cards = {}

    # From decks
    for deck in all_decks:
        all_entries = (
            deck.get("main_deck", [])
            + deck.get("sideboard", [])
            + deck.get("companions", [])
        )
        for entry in all_entries:
            cid = str(entry["cardId"])
            qty = entry.get("quantity", 1)
            info = card_db.get(int(cid), {})

            if cid not in all_cards:
                all_cards[cid] = {
                    "name": info.get("name", f"Unknown#{cid}"),
                    "type": info.get("type", ""),
                    "subtype": info.get("subtype", ""),
                    "mana": info.get("mana", ""),
                    "power": info.get("power", ""),
                    "toughness": info.get("toughness", ""),
                    "rarity": info.get("rarity", "unknown"),
                    "colors": info.get("colors", ""),
                    "max_qty": qty,
                    "seen_in_decks": [],
                    "source": "deck",
                }

            card = all_cards[cid]
            if qty > card["max_qty"]:
                card["max_qty"] = qty
            deck_name = deck["name"]
            if deck_name not in card.get("seen_in_decks", []):
                card.setdefault("seen_in_decks", []).append(deck_name)

    # From full collection (if available)
    if collection:
        for cid, count in collection.items():
            cid_str = str(cid)
            info = card_db.get(cid, {})
            if cid_str not in all_cards:
                all_cards[cid_str] = {
                    "name": info.get("name", f"Unknown#{cid}"),
                    "type": info.get("type", ""),
                    "subtype": info.get("subtype", ""),
                    "mana": info.get("mana", ""),
                    "power": info.get("power", ""),
                    "toughness": info.get("toughness", ""),
                    "rarity": info.get("rarity", "unknown"),
                    "colors": info.get("colors", ""),
                    "max_qty": count,
                    "seen_in_decks": [],
                    "source": "collection",
                }
            else:
                # Collection count is the real owned count
                all_cards[cid_str]["collection_count"] = count

    # Merge with existing (keep anything not in new data)
    for cid, info in existing.items():
        if cid not in all_cards:
            all_cards[cid] = info

    output = {
        "decks": deck_summaries,
        "all_cards": all_cards,
        "stats": {
            "total_unique_cards": len(all_cards),
            "total_decks": len(deck_summaries),
            "deck_names": list(deck_summaries.keys()),
            "has_full_collection": collection is not None,
        },
    }

    with open(RESOLVED_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return all_cards


def write_inventory(all_cards):
    """Write a human-readable inventory sorted by type then name."""
    cards = list(all_cards.values())

    type_order = [
        "Legendary Creature", "Legendary Enchantment Creature",
        "Creature", "Enchantment Creature",
        "Legendary Planeswalker", "Planeswalker",
        "Legendary Enchantment", "Enchantment",
        "Legendary Artifact", "Artifact", "Artifact Creature",
        "Instant", "Sorcery",
        "Land", "Legendary Land", "Basic Land",
    ]

    def sort_key(c):
        t = c.get("type", "")
        for i, prefix in enumerate(type_order):
            if t.startswith(prefix):
                return (i, c.get("name", ""))
        return (99, c.get("name", ""))

    cards.sort(key=sort_key)

    with open(INVENTORY_FILE, "w", encoding="utf-8") as f:
        f.write("# MTGA Card Inventory\n")
        f.write(f"# Total unique cards: {len(cards)}\n")
        f.write(f"# Generated by mtga_card_sync.py\n")
        f.write(f"# Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        current_type = ""
        for c in cards:
            t = c.get("type", "")
            if t != current_type:
                current_type = t
                sub = c.get("subtype", "")
                f.write(f"\n## {current_type}" + (f" {sub}" if sub else "") + "\n")
                f.write("-" * 40 + "\n")

            rarity = c.get("rarity", "?")[0].upper() if c.get("rarity") else "?"
            pt = f" {c['power']}/{c['toughness']}" if c.get("power") else ""
            decks = ", ".join(c.get("seen_in_decks", [])[:3])
            deck_str = f"  ({decks})" if decks else ""
            f.write(
                f"{c.get('max_qty', 1)}x [{rarity}] {c.get('name', '?')}"
                f" {c.get('mana', '')}{pt}{deck_str}\n"
            )


# ─── Live Watcher ────────────────────────────────────────────────────────────


def watch_log(existing_decks, card_db):
    """Watch the log file for new deck edits and collection data in real time."""
    print("\n" + "=" * 60)
    print("  Watching for new deck edits and collection data...")
    print("  (Edit a deck in Arena or log in to trigger captures)")
    print("  Press Ctrl+C to stop")
    print("=" * 60)

    last_size = os.path.getsize(LOG_PATH) if os.path.exists(LOG_PATH) else 0
    new_cards_found = 0
    all_decks = list(existing_decks)

    while True:
        try:
            if not os.path.exists(LOG_PATH):
                time.sleep(1)
                continue

            current_size = os.path.getsize(LOG_PATH)

            # Log file reset (Arena restarted)
            if current_size < last_size:
                print("\n  Log reset detected (Arena restarted)")
                last_size = 0

            if current_size <= last_size:
                time.sleep(0.5)
                continue

            with open(LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
                f.seek(last_size)
                new_content = f.read()
            last_size = current_size

            changed = False

            # Check for deck edits
            for line in new_content.split("\n"):
                if "DeckUpsertDeckV2" in line and "request" in line and "==>" in line:
                    deck = _parse_deck_line(line)
                    if deck:
                        # Replace existing deck with same name or add new
                        replaced = False
                        for i, d in enumerate(all_decks):
                            if d["name"] == deck["name"]:
                                all_decks[i] = deck
                                replaced = True
                                break
                        if not replaced:
                            all_decks.append(deck)

                        card_count = len(deck["main_deck"])
                        print(f"\n  Deck captured: \"{deck['name']}\" ({deck['total_cards']} cards, {card_count} unique)")
                        changed = True

            # Check for full collection dump
            if "GetPlayerCardsV3" in new_content:
                match = re.search(r"GetPlayerCardsV3.*?(\{.*\})", new_content, re.DOTALL)
                if match:
                    try:
                        data = json.loads(match.group(1))
                        collection = _filter_collection(data)
                        if collection and len(collection) > 50:
                            print(f"\n  FULL COLLECTION captured! {len(collection)} unique cards!")
                            all_ids = collect_all_card_ids(all_decks, collection)
                            new_db = resolve_card_ids(all_ids)
                            card_db.update(new_db)
                            save_collection_data(collection, card_db)
                            changed = True
                    except json.JSONDecodeError:
                        pass

            # Also catch large JSON blobs that look like collection data
            for line in new_content.split("\n"):
                line = line.strip()
                if not line.startswith("{"):
                    continue
                card_pattern = re.findall(r'"(\d{4,6})"\s*:\s*(\d+)', line)
                if len(card_pattern) > 200:
                    try:
                        data = json.loads(line)
                        collection = _filter_collection(data)
                        if collection and len(collection) > 200:
                            print(f"\n  Collection data detected! {len(collection)} cards")
                            all_ids = collect_all_card_ids(all_decks, collection)
                            new_db = resolve_card_ids(all_ids)
                            card_db.update(new_db)
                            save_collection_data(collection, card_db)
                            changed = True
                    except json.JSONDecodeError:
                        continue

            if changed:
                # Re-resolve and save everything
                all_ids = collect_all_card_ids(all_decks)
                new_ids = all_ids - set(card_db.keys())
                if new_ids:
                    new_resolved = resolve_card_ids(new_ids)
                    card_db.update(new_resolved)
                    print(f"  Resolved {len(new_resolved)} new card IDs")

                save_raw(all_decks, all_ids)
                all_cards = build_master_file(all_decks, card_db)
                write_inventory(all_cards)
                print(f"  Master file updated: {len(all_cards)} total unique cards")

        except KeyboardInterrupt:
            print("\n\nStopped watching. All data saved.")
            break


# ─── Main ────────────────────────────────────────────────────────────────────


def main():
    args = sys.argv[1:]
    scan_only = "--scan" in args
    watch_only = "--watch" in args

    print("=" * 60)
    print("  MTGA Card Sync — Collection & Deck Tracker")
    print("=" * 60)

    old_data = load_existing_raw()
    all_decks = old_data.get("decks", [])
    collection = None
    card_db = {}

    # ── Initial Scan ──
    if not watch_only:
        print("\n[1/4] Scanning log for deck edits...")
        new_decks = extract_decks_from_log()
        print(f"  Found {len(new_decks)} deck snapshots")

        if new_decks:
            all_decks = merge_decks(new_decks, old_data)

        print(f"\n[2/4] Checking for full collection dump...")
        collection = extract_collection_from_log()
        if collection:
            print(f"  Found full collection: {len(collection)} unique cards!")
        else:
            print("  No full collection dump found (triggers on Arena login)")

        all_ids = collect_all_card_ids(all_decks, collection)
        print(f"\n[3/4] Resolving {len(all_ids)} card IDs...")
        card_db = resolve_card_ids(all_ids)
        print(f"  Resolved {len(card_db)} cards")

        if collection:
            save_collection_data(collection, card_db)

        save_raw(all_decks, all_ids)

        print(f"\n[4/4] Building master files...")
        all_cards = build_master_file(all_decks, card_db, collection)
        write_inventory(all_cards)

        print(f"\n  {len(all_cards)} unique cards across {len(all_decks)} deck snapshots")
        print(f"  Files:")
        print(f"    {RAW_FILE}")
        print(f"    {RESOLVED_FILE}")
        print(f"    {INVENTORY_FILE}")

    # ── Watch Mode ──
    if not scan_only:
        watch_log(all_decks, card_db)
    else:
        print("\n  Done! (scan-only mode)")


if __name__ == "__main__":
    main()
