from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class ClientCreate(BaseModel):
    nombre: str
    email: EmailStr # Esto valida formato y lo hace obligatorio
    telefono: Optional[str] = None # Opcional
    empresa: Optional[str] = None
    notas: Optional[str] = None

class Client(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    telefono: Optional[str] = None
    empresa: Optional[str] = None
    notas: Optional[str] = None
    
    class Config:
        orm_mode = True

class ClientUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    notas: Optional[str] = None

class Clientes(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    telefono: Optional[str] = None
    empresa: Optional[str] = None
    notas: Optional[str] = None