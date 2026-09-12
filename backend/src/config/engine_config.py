from functools import lru_cache
from os import environ

from stoolap import Database

def _get_engine_stoolap() -> Database:
    base_dir = environ.get("BASE_DIR", "")
    bd_name = environ.get("BD_NAME", "")
    db = Database.open(f"{base_dir}/{bd_name}")
    return db

def _get_engine() -> Database:
    ambiente = environ.get("AMBIENTE", "")

    if ambiente.lower() == "stoolap":
        return _get_engine_stoolap()
    else:
        raise ValueError(f"AMBIENTE invalido: {ambiente}")

@lru_cache(maxsize=1)
def get_engine() -> Database:
    return _get_engine()