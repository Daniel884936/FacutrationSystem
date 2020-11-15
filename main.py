from fastapi import FastAPI, HTTPException
from sql_app import models, database
from routers import products

models.Base.metadata.create_all(bind= database.engine)

app = FastAPI()

app.include_router(
    products.router,
    prefix='/product',
    tags=['product'],
    responses={404:{"description": "Not found"}}
)

@app.get('/')
def root():
    return{'api':'facturationSystem'}
