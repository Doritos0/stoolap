from fastapi import APIRouter
from pydantic import BaseModel

from src.config.engine_config import get_engine

router = APIRouter(prefix="/productos", tags=["productos"])


class ProductoIn(BaseModel):
    nombre: str
    precio: float
    stock: int = 0


@router.get("")
def listar_productos():
    return get_engine().query("SELECT * FROM productos ORDER BY id")


@router.post("", status_code=201)
def crear_producto(producto: ProductoIn):
    return get_engine().query_one(
        "INSERT INTO productos (nombre, precio, stock) VALUES ($1, $2, $3) RETURNING *",
        [producto.nombre, producto.precio, producto.stock],
    )
