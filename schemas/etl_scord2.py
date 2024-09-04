from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class FichaInscripcion(BaseModel):
    id: int
    id_sede: int
    codigo_abonado: int
    fecha_aprobación: datetime
    estado_ficha: str
    fecha_ingreso: datetime
    fecha_insert: datetime
    class Config:
        orm_mode = True