from fastapi import FastAPI, HTTPException
from sql_app import models, database
from routers import products, invoice


models.Base.metadata.create_all(bind= database.engine)

app = FastAPI()

def routers(file, prefix:str, tags:str):
    app.include_router(
    file.router,
    prefix=f'/{prefix}',
    tags=[f'{tags}'],
    responses={404:{"description": "Not found"}})
    
routers(products,'products','products')
routers(invoice,'invoice','invoice')

@app.get('/')
def root():
    return{'api':'facturationSystem'}
