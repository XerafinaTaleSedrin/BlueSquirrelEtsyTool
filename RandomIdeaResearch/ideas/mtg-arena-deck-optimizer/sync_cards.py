"""
MTGA Card Sync
==============
Scans the MTGA Player.log for ALL deck data (DeckUpsertDeckV2 events),
resolves card IDs to names via the local SQLite card database,
and merges everything into persistent master files.

Run this anytime after editing decks in Arena to keep the card database current.

Usage:
    python sync_cards.py

Output files:
    deck_data_raw.json       - Raw deck dumps with card IDs and quantities
    all_cards_resolved.json  - Master card database with names, types, mana costs
    card_inventory.txt       - Human-readable card list (Arena import format)
"""

import json
import os
import sys
import sqlite3
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.expandvars(
    r"%APPDATA%\..\LocalLow\Wizards Of The Coast\MTGA\Player.log"
)
CARD_DB_DIR = r"C:\Program Files (x86)\Steam\steamapps\common\MTGA\MTGA_Data\Downloads\Raw"
RAW_FILE = os.path.join(SCRIPT_DIR, "deck_data_raw.json")
RESOLVED_FILE = os.path.join(SCRIPT_DIR, "all_cards_resolved.json")
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "card_inventory.txt")


def find_card_database():
    """Find the MTGA SQLite card database file."""
    for f in os.listdir(CARD_DB_DIR):
        if "CardDatabase" in f and f.endswith(".mtga"):
            return os.path.join(CARD_DB_DIR, f)
    return None


def extract_decks_from_log():
    """Extract all deck data from the MTGA Player.log."""
    if not os.path.exists(LOG_PATH):
        print(f"ERROR: Player.log not found at {LOG_PATH}")
        return []

    print(f"Scanning: {LOG_PATH}")
    decks = []

    with open(LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f):
            if "DeckUpsertDeckV2" not in line:
                continue
            if "request" not in line or "==>" not in line:
                continue

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
                    decks.append({
                        "name": name,
                        "format": "Historic",
                        "main_deck": main_deck,
                        "sideboard": sideboard,
                        "companions": companions,
                        "total_cards": total,
                        "log_line": i,
                    })
            except (json.JSONDecodeError, ValueError, KeyError):
                continue

    print(f"  Found {len(decks)} deck snapshots in log")
    return decks


def merge_with_existing(new_decks):
    """Merge new deck data with any existing saved data."""
    all_decks = list(new_decks)

    # Load existing raw data and keep decks not found in new log
    if os.path.exists(RAW_FILE):
        with open(RAW_FILE, "r") as f:
            old_data = json.load(f)

        new_names = {d["name"] for d in new_decks}
        for deck in old_data.get("decks", []):
            if deck.get("name") not in new_names:
                all_decks.append(deck)
                print(f"  Kept from previous save: {deck['name']}")

    # Collect all unique card IDs
    all_ids = set()
    for deck in all_decks:
        for entry in deck.get("main_deck", []):
            all_ids.add(entry["cardId"])
        for entry in deck.get("sideboard", []):
            all_ids.add(entry["cardId"])
        for entry in deck.get("companions", []):
            all_ids.add(entry["cardId"])

    # Save raw data
    output = {
        "decks": all_decks,
        "unique_card_ids": sorted(list(all_ids)),
    }
    with open(RAW_FILE, "w") as f:
        json.dump(output, f, indent=2)

    print(f"  Saved {len(all_decks)} decks, {len(all_ids)} unique card IDs")
    return all_decks, all_ids


def resolve_card_ids(card_ids):
    """Resolve card IDs to names using the MTGA SQLite database."""
    db_path = find_card_database()
    if not db_path:
        print("ERROR: Could not find MTGA card database")
        return {}

    print(f"Resolving {len(card_ids)} card IDs...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    placeholders = ",".join(["?" for _ in card_ids])
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
        list(card_ids),
    )

    rarity_map = {0: "common", 1: "uncommon", 2: "rare", 3: "mythic"}
    card_db = {}
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
    print(f"  Resolved {len(card_db)} cards")
    return card_db


def build_master_file(all_decks, card_db):
    """Build the master resolved card file."""
    # Load existing resolved data to preserve any manually added info
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

    # Build master card list (max quantity seen across all decks)
    all_cards = {}
    for deck in all_decks:
        for entry in deck.get("main_deck", []) + deck.get("sideboard", []) + deck.get("companions", []):
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
                }

            card = all_cards[cid]
            if qty > card["max_qty"]:
                card["max_qty"] = qty

            deck_name = deck["name"]
            if deck_name not in card["seen_in_decks"]:
                card["seen_in_decks"].append(deck_name)

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
        },
    }

    with open(RESOLVED_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"  Master file: {len(all_cards)} unique cards across {len(deck_summaries)} decks")
    return all_cards


def write_inventory(all_cards):
    """Write a human-readable inventory sorted by color and type."""
    cards = list(all_cards.values())

    # Sort: by type (Creature, Enchantment, etc.) then name
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
        t = c["type"]
        for i, prefix in enumerate(type_order):
            if t.startswith(prefix):
                return (i, c["name"])
        return (99, c["name"])

    cards.sort(key=sort_key)

    with open(INVENTORY_FILE, "w", encoding="utf-8") as f:
        f.write("# MTGA Card Inventory\n")
        f.write(f"# Total unique cards: {len(cards)}\n")
        f.write(f"# Generated by sync_cards.py\n\n")

        current_type = ""
        for c in cards:
            t = c["type"]
            if t != current_type:
                current_type = t
                f.write(f"\n## {current_type} {c.get('subtype', '')}\n")
                f.write("-" * 40 + "\n")

            rarity = c["rarity"][0].upper() if c["rarity"] else "?"
            pt = f" {c['power']}/{c['toughness']}" if c["power"] else ""
            decks = ", ".join(c.get("seen_in_decks", [])[:3])
            f.write(
                f"{c['max_qty']}x [{rarity}] {c['name']}"
                f" {c['mana']}{pt}"
                f"  ({decks})\n"
            )

    print(f"  Inventory written to {INVENTORY_FILE}")


def main():
    print("=" * 60)
    print("  MTGA Card Sync")
    print("=" * 60)

    # Step 1: Extract from log
    new_decks = extract_decks_from_log()
    if not new_decks:
        print("\nNo deck data found in player log.")
        print("Open a deck in Arena's deck builder to generate data.")
        return

    # Step 2: Merge with existing
    all_decks, all_ids = merge_with_existing(new_decks)

    # Step 3: Resolve card IDs
    card_db = resolve_card_ids(all_ids)

    # Step 4: Build master file
    all_cards = build_master_file(all_decks, card_db)

    # Step 5: Write human-readable inventory
    write_inventory(all_cards)

    print("\n" + "=" * 60)
    print(f"  Done! {len(all_cards)} cards tracked across {len(all_decks)} deck snapshots")
    print(f"  Files updated:")
    print(f"    {RAW_FILE}")
    print(f"    {RESOLVED_FILE}")
    print(f"    {INVENTORY_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
