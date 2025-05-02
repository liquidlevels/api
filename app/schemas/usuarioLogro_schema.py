from pydantic import BaseModel
from datetime import datetime

class UsuarioLogroBase(BaseModel):
    usuario_id: int
    logro_id: int

class UsuarioLogroCreate(UsuarioLogroBase):
    pass  # igual al base

class UsuarioLogroOut(UsuarioLogroBase):
    fecha: datetime

    class Config:
        orm_mode = True
