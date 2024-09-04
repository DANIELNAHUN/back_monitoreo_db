from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Text, DateTime, Date, Float

from config.db import Base

class FichaInscripcion(Base):
    __tablename__ = "ficha_inscripcion"

    id = Column(Integer, primary_key=True, index=True)
    id_sede = Column(Integer)
    codigo_abonado = Column(Integer)
    fecha_aprobacion = Column(DateTime)
    estado_ficha = Column(String(50))
    fecha_ingreso = Column(DateTime)
    fecha_insert = Column(DateTime)