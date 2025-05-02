from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional

# Base con los campos comunes
class AmistadBase(BaseModel):
    usuario_id: int
    amigo_id: int
    estado: constr(strip_whitespace=True, min_length=1, max_length=20)  # pendiente, aceptado, bloqueado

# Para crear una solicitud de amistad
class AmistadCreate(AmistadBase):
    pass

# Para actualizar el estado de la relación
class AmistadUpdate(BaseModel):
    estado: constr(strip_whitespace=True, min_length=1, max_length=20)

# Para mostrar amistad en respuesta
class AmistadOut(AmistadBase):
    fecha_creacion: datetime

    class Config:
        orm_mode = True
