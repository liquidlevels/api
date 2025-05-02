from pydantic import BaseModel
from typing import Optional

class DireccionOut(BaseModel):
    id_establecimiento: int
    cod_postal: Optional[str]
    nom_vial: Optional[str]
    numero_est: Optional[str]
    edificio: Optional[str]
    asentamiento: Optional[str]
    municipio: Optional[str]
    localidad: Optional[str]

    class Config:
        orm_mode = True
