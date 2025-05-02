from pydantic import BaseModel, EmailStr, HttpUrl, constr, Field
from typing import Optional

class UsuarioBase(BaseModel):
    nombre:constr(strip_whitespace=True, min_length=1, max_length=50)
    apellido: constr(strip_whitespace=True, min_length=1, max_length=50)
    email: EmailStr
    telefono: constr(strip_whitespace=True, min_length=7, max_length=15, regex=r'^\+?\d{7,15}$')  
    foto: Optional[HttpUrl]  
    rol_id: int = Field(..., gt=0)  

class UsuarioCreate(UsuarioBase):
    pass  # igual a base

class UsuarioUpdate(BaseModel):
    nombre: Optional[constr(strip_whitespace=True, min_length=1, max_length=50)]
    apellido: Optional[constr(strip_whitespace=True, min_length=1, max_length=50)]
    email: Optional[EmailStr]
    telefono: Optional[constr(strip_whitespace=True, min_length=7, max_length=15, regex=r'^\+?\d{7,15}$')]
    foto: Optional[HttpUrl]
    rol_id: Optional[int] = Field(None, gt=0)

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
