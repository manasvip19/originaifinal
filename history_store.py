import json
from datetime import datetime
from pathlib import Path

STORE_PATH = Path("uploads") / "analysis_history.json"
STORE_PATH.parent.mkdir(parents=True, exist_ok=True)


def _load():
    if not STORE_PATH.exists():
        return []
    try:
        with STORE_PATH.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except Exception:
        return []


def _save(entries):
    with STORE_PATH.open("w", encoding="utf-8") as handle:
        json.dump(entries, handle, indent=2)


def add_entry(entry):
    entries = _load()
    entries.insert(0, entry)
    _save(entries)


def latest_entry():
    entries = _load()
    return entries[0] if entries else None


def all_entries():
    return _load()
