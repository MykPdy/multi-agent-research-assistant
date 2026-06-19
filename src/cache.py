import json
import hashlib
from pathlib import Path


CACHE_DIR = Path("cache")

CACHE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def _cache_key(query: str) -> str:
    return hashlib.md5(
        query.lower().strip().encode()
    ).hexdigest()


def get_cached_result(query: str):
    key = _cache_key(query)

    cache_file = CACHE_DIR / f"{key}.json"

    if not cache_file.exists():
        return None

    with open(cache_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cached_result(
    query: str,
    result: dict
):
    key = _cache_key(query)

    cache_file = CACHE_DIR / f"{key}.json"

    with open(
        cache_file,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            result,
            f,
            indent=2,
            ensure_ascii=False
        )