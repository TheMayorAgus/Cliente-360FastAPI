from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Cliente(Base):
    __tablename__= "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    empresa = Column(String, nullable=True) 
    notas = Column(String, nullable=True)