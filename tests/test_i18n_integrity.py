import json
from pathlib import Path


def load_keys(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return set(data.keys())


def test_translation_key_sets_match():
    base = Path("static/translations/en.json")
    assert base.exists()
    base_keys = load_keys(base)

    for other in ["hi.json", "te.json", "ta.json"]:
        p = Path("static/translations") / other
        assert p.exists(), f"Missing translation file: {other}"
        keys = load_keys(p)
        missing = base_keys - keys
        assert not missing, f"Translation {other} is missing keys: {sorted(list(missing))[:5]}..."
