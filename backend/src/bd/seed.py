from pathlib import Path

from dotenv import load_dotenv
from stoolap import Database

from src.config.engine_config import get_engine

NOMBRES = [
    "Ana", "Luis", "Carla", "Pedro", "Sofia", "Diego", "Valentina", "Matias", "Camila", "Jose",
    "Fernanda", "Tomas", "Isidora", "Benjamin", "Martina", "Joaquin", "Antonia", "Vicente", "Catalina", "Felipe",
]
APELLIDOS = [
    "Gonzalez", "Munoz", "Rojas", "Diaz", "Perez", "Soto", "Contreras", "Silva", "Martinez", "Sepulveda",
    "Morales", "Rodriguez", "Lopez", "Fuentes", "Hernandez",
]
USUARIOS = [
    [f"{nombre} {apellido}", f"{nombre.lower()}.{apellido.lower()}@mail.com"]
    for nombre in NOMBRES
    for apellido in APELLIDOS
]

TIPOS = [
    "Teclado", "Mouse", "Monitor", "Notebook", "Audifonos", "Parlante", "Webcam", "Microfono", "Impresora", "Router",
    "Disco SSD", "Pendrive", "Tablet", "Celular", "Cargador", "Cable HDMI", "Silla Gamer", "Escritorio", "Lampara LED", "Mousepad",
]
MARCAS = ["Logitech", "HP", "Lenovo", "Samsung", "Asus", "Acer", "Xiaomi", "Sony", "Dell", "Razer"]
PRODUCTOS = [
    [f"{tipo} {marca}", round(5 + (i * 37) % 500 + 0.99, 2), (i * 13) % 100]
    for i, (tipo, marca) in enumerate((tipo, marca) for tipo in TIPOS for marca in MARCAS)
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
