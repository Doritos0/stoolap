from pathlib import Path

from dotenv import load_dotenv
from stoolap import Database

from config.engine_config import get_engine

USUARIOS = [
    ["Ana", "ana@mail.com"],
    ["Luis", "luis@mail.com"],
    ["Carla", "carla@mail.com"],
]

PRODUCTOS = [
    ["Teclado", 25.5, 10],
    ["Mouse", 12.0, 30],
    ["Monitor", 180.0, 5],
]


def llenar_tablas(db: Database) -> None:
    if db.query_one("SELECT COUNT(*) AS n FROM usuarios")["n"] == 0:
        db.execute_batch("INSERT INTO usuarios (nombre, email) VALUES ($1, $2)", USUARIOS)
    if db.query_one("SELECT COUNT(*) AS n FROM productos")["n"] == 0:
        db.execute_batch("INSERT INTO productos (nombre, precio, stock) VALUES ($1, $2, $3)", PRODUCTOS)


if __name__ == "__main__":
    load_dotenv(Path(__file__).parent.parent / ".env-desarrollo")
    llenar_tablas(get_engine())
    print("Tablas llenadas")
