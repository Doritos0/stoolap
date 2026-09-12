from pathlib import Path

from dotenv import load_dotenv

local_path = Path(__file__).parent
env_file = local_path / ".env-desarrollo"
load_dotenv(env_file)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config.engine_config import get_engine

title = "Prueba Stoolap"
version = "0.1.0"
descripcion = """
Prueba base de datos Stoolap
"""

app = FastAPI(title=title, version=version, description=descripcion, docs_url="/swagger", root_path="/api")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


class UsuarioIn(BaseModel):
    nombre: str
    email: str


class ProductoIn(BaseModel):
    nombre: str
    precio: float
    stock: int = 0


@app.get("/usuarios")
def listar_usuarios():
    return get_engine().query("SELECT * FROM usuarios ORDER BY id")


@app.post("/usuarios", status_code=201)
def crear_usuario(usuario: UsuarioIn):
    return get_engine().query_one(
        "INSERT INTO usuarios (nombre, email) VALUES ($1, $2) RETURNING *",
        [usuario.nombre, usuario.email],
    )


@app.get("/productos")
def listar_productos():
    return get_engine().query("SELECT * FROM productos ORDER BY id")


@app.post("/productos", status_code=201)
def crear_producto(producto: ProductoIn):
    return get_engine().query_one(
        "INSERT INTO productos (nombre, precio, stock) VALUES ($1, $2, $3) RETURNING *",
        [producto.nombre, producto.precio, producto.stock],
    )