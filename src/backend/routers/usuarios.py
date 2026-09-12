from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from src.config.engine_config import get_engine

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


class UsuarioIn(BaseModel):
    nombre: str
    email: str

class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: str
    creado: datetime


@router.get("")
def listar_usuarios() -> list[UsuarioOut]:
    return get_engine().query("SELECT * FROM usuarios ORDER BY id")


@router.post("", status_code=201)
def crear_usuario(usuario: UsuarioIn):
    return get_engine().query_one(
        "INSERT INTO usuarios (nombre, email) VALUES ($1, $2) RETURNING *",
        [usuario.nombre, usuario.email],
    )
