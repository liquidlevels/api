from pydantic import BaseModel, condecimal
from typing import Optional

class EstablecimientoOut(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str]
    latitud: condecimal(ge=-90, le=90, max_digits=8, decimal_places=6)
    longitud: condecimal(ge=-180, le=180, max_digits=9, decimal_places=6)
    usuario_empresa_id: int
    codigo_qr: Optional[str]
    estado: str

    class Config:
        orm_mode = True
