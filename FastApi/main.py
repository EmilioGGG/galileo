from enum import Enum
from random import random
from typing import Optional

from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, Query

from fastapi.responses import ORJSONResponse
from fastapi.responses import UJSONResponse
from starlette.responses import HTMLResponse, PlainTextResponse, RedirectResponse, StreamingResponse, FileResponse

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Arreglo Matematico"}

@app.get("/matematica/array")
def array(numeros: Optional[List[int]] = Query(None)):
    query_items = {"Numeros Ingresados": numeros}
    sumatoria  = 0
    resta = 0
    multip = 0
    divis = 0
    for i in range(len(numeros)):
        if i == 0:
            sumatoria = numeros[i]
            resta = numeros[i]
            multip = numeros[i]
            divis = numeros[i]
        else:
            sumatoria+= numeros[i]
            resta-= numeros[i]
            multip*=numeros[i]
            divis /= numeros[i]

    #sumatoria-= numeros[0]
    #resta+= numeros[0]
    return {'Suma de los numeros: ': sumatoria, 'Resta de los numeros:': resta,'Multiplicacion de los numeros: ': multip, 'Division de los numeros:': divis}

