from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List, Optional
import io
import json
from datetime import datetime, timedelta
from app.db.database import get_db
from app.schemas.cliente_schema import Client, ClientCreate, ClientUpdate
from app.models.cliente import Cliente

api_router = APIRouter()

# Endpoint de eventos
@api_router.get("/clientes", response_model=List[Client])
def read_clientes(db: Session = Depends(get_db)):
    # Obtener lista de clientes
    clientes = db.query(Cliente).all()
    return clientes
    
@api_router.get("/clientes/{id}")
def read_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario Inexistente"
        )
    return cliente

@api_router.post("/clientes", response_model=Client, status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente: ClientCreate, response: Response, db: Session = Depends(get_db)):
    # Verificar si el email ya existe
    if db.query(Cliente).filter(Cliente.email == cliente.email).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El Email ya está registrado"
        )
    # Crear cliente
    nuevo_cliente = Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    response.headers["Location"] = f"/clientes/{nuevo_cliente.id}"
    return nuevo_cliente 
    

@api_router.put("/clientes/{id}", response_model=Client)
def update_cliente(id: int, cliente: ClientUpdate, db: Session = Depends(get_db)):

        cliente_existente = db.query(Cliente).filter(Cliente.id == id).first()
        if not cliente_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente no encontrado"
        )
        cliente_existente.email = cliente.email
        cliente_existente.nombre = cliente.nombre
        cliente_existente.telefono = cliente.telefono
        cliente_existente.notas = cliente.notas
        db.commit()
        db.refresh(cliente_existente)
        return cliente_existente    

@api_router.delete("/clientes/{id}", response_model=Client)
def delete_cliente(id: int, db: Session = Depends(get_db)):
        cliente_existente = db.query(Cliente).filter(Cliente.id == id).first()
        if not cliente_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cliente no encontrado"
        )
        db.delete(cliente_existente)
        db.commit()
        return {"mensaje": "borrado con éxito"} 