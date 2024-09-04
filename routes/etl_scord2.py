from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session
import pandas as pd
from datetime import datetime
import numpy as np

from models import etl_scord2 as etl_scord2_model
from schemas import etl_scord2 as etl_scord2_schema
from config import db as confdb

route_etl = APIRouter()

def get_db():
    db = confdb.SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependecy = Annotated[Session, Depends(get_db)]

# FICHA INSCRIPCION
@route_etl.get("/validacion/", response_model=List[dict])
async def validation_ficha(db: db_dependecy):
    result = db.query(etl_scord2_model.FichaInscripcion).all()
    data = [record.__dict__ for record in result]
    for item in data:
        item.pop('_sa_instance_state', None)
    dfFicha = pd.DataFrame.from_records(data)
    hoy = datetime.now().date()
    fechahora_final = datetime.now()
    fechahora_final = fechahora_final.strftime("%Y-%m-%d 19:00:00")
    dfFicha['fecha_ingreso'] = pd.to_datetime(dfFicha['fecha_ingreso']).dt.date
    dfFicha['fecha_insert'] = pd.to_datetime(dfFicha['fecha_insert']).dt.date
    dfFicha['actualizado_ingreso'] = np.where(dfFicha['fecha_ingreso'] == hoy, '1', '0')
    dfFicha['actualizado_insert'] = np.where(dfFicha['fecha_insert'] > fechahora_final, '1', '0')
    
    return result