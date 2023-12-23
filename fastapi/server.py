import shutil

import io
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile,Form
import pandas as pd
from typing import  List

from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Contrato(BaseModel):
    Beverage_category: str
    Beverage: str
    Beverage_prep: str
    Calories: int
    Total_Fat_g: float
    Trans_Fat_g: float
    Saturated_Fat_g: float
    Sodium_mg: int
    Total_Carbohydrates_g: int
    Cholesterol_mg: int
    Dietary_Fibre_g: int
    Sugars_g: int
    Protein_g: float
    Vitamin_A_percent_DV: str
    Vitamin_C_percent_DV: str
    Calcium_percent_DV: str
    Iron_percent_DV: str
    Caffeine_mg: int

class ListadoContratos(BaseModel):
    contratos = List[Contrato]

app = FastAPI(
    title="Servidor de datos",
    version="0.1.0",
)


@app.get("/retrieve_data/")
#def insercion_endpoint (titulo:str = Form(...), autor:str=Form(...), pais:str=Form(...),genero:str=File(...),  archivo: UploadFile=File(...)):
def retrieve_data ():
    todosmisdatos = pd.read_csv('./starbucks.csv',sep=',')
    todosmisdatos = todosmisdatos.fillna(0)
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = ListadoContratos()
    listado.contratos = todosmisdatosdict
    return listado