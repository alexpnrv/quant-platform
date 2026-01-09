import json
from quant_platform.config import DATA_DIR

CACHE_FILE = DATA_DIR / 'market_cache.json'

def save_cache(data: dict) -> None:
    with open(CACHE_FILE, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_cache() -> dict:
    if CACHE_FILE.exists():
        with open(CACHE_FILE, 'r', encoding="utf-8") as f:
            return json.load(f)
    return {}