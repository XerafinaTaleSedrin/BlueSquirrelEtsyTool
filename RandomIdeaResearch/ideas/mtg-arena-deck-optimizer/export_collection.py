"""
MTGA Collection Exporter
========================
Watches the MTGA Player.log for your card collection data.

Usage:
  1. Close MTGA completely
  2. Run this script: python export_collection.py
  3. Open MTGA and log in
  4. Wait for the script to say "Done!"
  5. Your collection will be saved to my_collection.txt
"""

import json
import os
import re
import time
import sys

LOG_PATH = os.path.expandvars(
    r"%APPDATA%\..\LocalLow\Wizards Of The Coast\MTGA\Player.log"
)
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "my_collection.txt")
OUTPUT_JSON = os.path.join(os.path.dirname(__file__), "my_collection.json")

# MTGA card database for resolving grpIds to names
CARD_DB_DIR = r"C:\Program Files (x86)\Steam\steamapps\common\MTGA\MTGA_Data\Downloads\Raw"


def load_card_database():
    """Try to load MTGA's card database to resolve grpIds to card names."""
    print("Loading MTGA card database...")

    # Find the CardDatabase file
    card_db_path = None
    for f in os.listdir(CARD_DB_DIR):
        if "CardDatabase" in f:
            card_db_path = os.path.join(CARD_DB_DIR, f)
            break

    if not card_db_path:
        print("  Warning: Could not find CardDatabase file")
        return {}

    try:
        with open(card_db_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Try parsing as JSON
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            # Sometimes the file has a BOM or other prefix
            # Try to find the JSON start
            json_start = content.find("[")
            if json_start == -1:
                json_start = content.find("{")
            if json_start >= 0:
                data = json.loads(content[json_start:])
            else:
                print("  Warning: Could not parse CardDatabase as JSON")
                return {}

        # Build grpId -> card name mapping
        card_map = {}
        if isinstance(data, list):
            for entry in data:
                if isinstance(entry, dict):
                    grp_id = entry.get("grpid") or entry.get("GrpId") or entry.get("grpId")
                    # Try various name fields
                    name = (entry.get("titleId") or entry.get("Title") or
                            entry.get("name") or entry.get("Name") or
                            entry.get("cardName") or "")
                    if grp_id and name:
                        card_map[grp_id] = entry
        elif isinstance(data, dict):
            # Might be keyed by grpId
            for key, entry in data.items():
                if isinstance(entry, dict):
                    card_map[key] = entry

        print(f"  Loaded {len(card_map)} cards from database")
        return card_map
    except Exception as e:
        print(f"  Warning: Error loading card database: {e}")
        return {}


def try_scryfall_bulk(arena_ids):
    """Use Scryfall's bulk data to resolve Arena IDs."""
    import urllib.request

    print(f"Resolving {len(arena_ids)} card IDs via Scryfall...")
    print("  Downloading Scryfall bulk data (this may take a moment)...")

    # Get the bulk data download URL
    try:
        req = urllib.request.Request(
            "https://api.scryfall.com/bulk-data/default-cards",
            headers={"Accept": "application/json"}
        )
        with urllib.request.urlopen(req) as resp:
            bulk_info = json.loads(resp.read())
            download_url = bulk_info["download_uri"]
    except Exception as e:
        print(f"  Could not get Scryfall bulk data URL: {e}")
        return {}

    # Download and parse - this is a large file
    try:
        req = urllib.request.Request(download_url)
        with urllib.request.urlopen(req) as resp:
            print("  Downloading... (this is ~80MB, please wait)")
            raw = resp.read()
            cards = json.loads(raw)

        # Build arena_id -> card info mapping
        arena_map = {}
        for card in cards:
            aid = card.get("arena_id")
            if aid and aid in arena_ids:
                arena_map[aid] = {
                    "name": card.get("name", "Unknown"),
                    "mana_cost": card.get("mana_cost", ""),
                    "type_line": card.get("type_line", ""),
                    "set": card.get("set", "").upper(),
                    "rarity": card.get("rarity", ""),
                    "colors": card.get("colors", []),
                }

        print(f"  Resolved {len(arena_map)} cards via Scryfall")
        return arena_map
    except Exception as e:
        print(f"  Error downloading Scryfall data: {e}")
        return {}


def watch_log_for_collection():
    """Watch the Player.log file for collection data."""

    print(f"\nWatching: {LOG_PATH}")
    print("=" * 60)
    print("Now open MTGA and log in.")
    print("The script will capture your collection automatically.")
    print("Press Ctrl+C to cancel.")
    print("=" * 60)

    # Track file position
    last_size = 0
    if os.path.exists(LOG_PATH):
        last_size = os.path.getsize(LOG_PATH)

    collected_data = None

    while True:
        try:
            if not os.path.exists(LOG_PATH):
                time.sleep(1)
                continue

            current_size = os.path.getsize(LOG_PATH)

            # File got smaller = Arena restarted, reset
            if current_size < last_size:
                print("\n  Log file reset detected (Arena restarted)")
                last_size = 0

            if current_size > last_size:
                with open(LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
                    f.seek(last_size)
                    new_content = f.read()

                last_size = current_size

                # Look for inventory/collection patterns
                # Pattern 1: PlayerInventory.GetPlayerCardsV3 response
                if "GetPlayerCardsV3" in new_content:
                    print("\n  Found GetPlayerCardsV3 response!")
                    match = re.search(r'GetPlayerCardsV3.*?(\{.*\})', new_content, re.DOTALL)
                    if match:
                        try:
                            collected_data = json.loads(match.group(1))
                            break
                        except json.JSONDecodeError:
                            pass

                # Pattern 2: Large JSON with card IDs (numbered keys with counts)
                # This is the format: {"12345": 4, "23456": 2, ...}
                for line in new_content.split("\n"):
                    line = line.strip()
                    if not line.startswith("{"):
                        continue

                    # Check if this looks like a card collection
                    # (large JSON object with numeric keys and small numeric values)
                    card_pattern = re.findall(r'"(\d{4,6})"\s*:\s*(\d+)', line)
                    if len(card_pattern) > 50:  # Likely a collection if 50+ card entries
                        print(f"\n  Found potential collection data! ({len(card_pattern)} card entries)")
                        try:
                            collected_data = json.loads(line)
                            # Verify it's actually cards (values should be 1-4 mostly)
                            values = list(collected_data.values()) if isinstance(collected_data, dict) else []
                            if values and all(isinstance(v, int) for v in values[:20]):
                                print(f"  Confirmed: {len(collected_data)} unique cards")
                                break
                        except json.JSONDecodeError:
                            pass

                if collected_data:
                    break

                # Pattern 3: Look for deck list responses that have card data
                if "DeckGetDeckListsV3" in new_content or "Deck.GetDeckLists" in new_content:
                    print("\n  Found deck list data (not full collection, but useful)")

                # Show progress dots
                sys.stdout.write(".")
                sys.stdout.flush()

            time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n\nCancelled by user.")
            return None

    return collected_data


def parse_existing_log():
    """Parse the existing log file for any collection data already present."""
    if not os.path.exists(LOG_PATH):
        return None

    print(f"Scanning existing log for collection data...")

    with open(LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Look for large JSON objects with numeric keys (card collections)
    for line in content.split("\n"):
        line = line.strip()
        if not line.startswith("{"):
            continue

        card_pattern = re.findall(r'"(\d{4,6})"\s*:\s*(\d+)', line)
        if len(card_pattern) > 50:
            try:
                data = json.loads(line)
                values = list(data.values()) if isinstance(data, dict) else []
                # Filter to only numeric key-value pairs (card ID -> count)
                card_data = {}
                for k, v in data.items():
                    if k.isdigit() and isinstance(v, int) and v > 0:
                        card_data[k] = v

                if len(card_data) > 50:
                    print(f"  Found existing collection: {len(card_data)} unique cards")
                    return card_data
            except json.JSONDecodeError:
                continue

    return None


def save_collection(collection, card_db=None):
    """Save the collection to files."""

    # Save raw JSON
    with open(OUTPUT_JSON, "w") as f:
        json.dump(collection, f, indent=2)
    print(f"\nRaw collection saved to: {OUTPUT_JSON}")

    # Save readable text
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# MTGA Collection Export\n")
        f.write(f"# Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"# Total unique cards: {len(collection)}\n")
        f.write(f"# Total card count: {sum(collection.values())}\n\n")

        if card_db:
            # Write with resolved names
            for card_id, count in sorted(collection.items()):
                info = card_db.get(int(card_id), card_db.get(card_id, None))
                if info:
                    name = info.get("name", info.get("Name", f"Card #{card_id}"))
                    f.write(f"{count} {name}\n")
                else:
                    f.write(f"{count} [Arena ID: {card_id}]\n")
        else:
            # Write with just IDs
            for card_id, count in sorted(collection.items()):
                f.write(f"{count} [Arena ID: {card_id}]\n")

    print(f"Collection list saved to: {OUTPUT_FILE}")


def main():
    print("=" * 60)
    print("  MTGA Collection Exporter")
    print("=" * 60)

    # First check if collection data already exists in current log
    collection = parse_existing_log()

    if not collection:
        print("\nNo collection data found in current log.")
        print("Will watch for it on next login.\n")
        collection = watch_log_for_collection()

    if not collection:
        print("No collection data captured. Exiting.")
        return

    print(f"\nCollection captured: {len(collection)} unique cards!")

    # Try to load card database for name resolution
    card_db = {}
    try:
        card_db = load_card_database()
    except Exception as e:
        print(f"Could not load card database: {e}")

    # Save results
    save_collection(collection, card_db)

    print("\n" + "=" * 60)
    print("Done! Paste the contents of my_collection.txt to Claude")
    print("for deck building recommendations.")
    print("=" * 60)


if __name__ == "__main__":
    main()
