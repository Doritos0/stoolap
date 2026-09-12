from pathlib import Path

from dotenv import load_dotenv

local_path = Path(__file__).parent
env_file = local_path / ".env-desarrollo"
load_dotenv(env_file)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.backend.routers import productos, usuarios

title = "Prueba Stoolap"
version = "0.1.0"
descripcion = """
Prueba base de datos Stoolap
"""

app = FastAPI(title=title, version=version, description=descripcion, docs_url="/swagger", root_path="/api")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(usuarios.router)
app.include_router(productos.router)