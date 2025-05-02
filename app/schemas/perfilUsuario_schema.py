from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime

class PerfilUsuarioBase(BaseModel):
    nivel_usuario: constr(strip_whitespace=True, min_length=1, max_length=50)

class PerfilUsuarioCreate(PerfilUsuarioBase):
    usuario_id: int

class PerfilUsuarioUpdate(BaseModel):
    nivel_usuario: Optional[constr(strip_whitespace=True, min_length=1, max_length=50)] = None

class PerfilUsuarioOut(PerfilUsuarioBase):
    usuario_id: int
    fecha_creacion: datetime

    class Config:
        orm_mode = True
