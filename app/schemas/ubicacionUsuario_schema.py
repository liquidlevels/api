from pydantic import BaseModel, Field, condecimal
from datetime import datetime
from typing import Optional

# Base
class UbicacionUsuarioBase(BaseModel):
    latitud: condecimal(ge=-90, le=90, max_digits=8, decimal_places=6)
    longitud: condecimal(ge=-180, le=180, max_digits=9, decimal_places=6)

# Para crear o actualizar la ubicación
class UbicacionUsuarioCreate(UbicacionUsuarioBase):
    usuario_id: int

# Para salida de datos
class UbicacionUsuarioOut(UbicacionUsuarioCreate):
    ultima_actualizacion: datetime

    class Config:
        orm_mode = True
