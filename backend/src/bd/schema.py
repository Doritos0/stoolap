from pathlib import Path

from dotenv import load_dotenv
from stoolap import Database

from config.engine_config import get_engine

TABLAS = [
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        creado TIMESTAMP DEFAULT NOW()
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        nombre TEXT NOT NULL,
        precio FLOAT NOT NULL,
        stock INTEGER DEFAULT 0,
        creado TIMESTAMP DEFAULT NOW()
    )
    """,
]


def crear_estructura(db: Database) -> None:
    for sql in TABLAS:
        db.exec(sql)


if __name__ == "__main__":
    load_dotenv(Path(__file__).parent.parent / ".env-desarrollo")
    crear_estructura(get_engine())
    print("Estructura creada")
