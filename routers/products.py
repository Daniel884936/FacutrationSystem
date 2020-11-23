from fastapi import APIRouter, Depends, HTTPException
from dependencies.database import get_db
from sqlalchemy.orm import Session
from starlette import status
from sql_app import shemas, crud
from resources import strings
from sql_app.shemas import ServerResponse
router = APIRouter()

@router.post('/create')
def create_product(product: shemas.ProductCreate ,db: Session  = Depends(get_db)):
    crud.create_products(db, product)
    return ServerResponse(msg=strings.CREATED)


@router.get('/get')
def get_all_products(db: Session  = Depends(get_db)):
    products = crud.get_all_products(db)
    if not products:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                            detail=strings.PRODUCTS_NOT_FOUND)
    return ServerResponse(msg=strings.SUCCESS, data=products)


@router.put('/update')
def update_prodcut(product:shemas.ProductUpdate,db: Session  = Depends(get_db)):
    product_updated =  crud.update_product(db,product)
    if not product_updated:
       raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                           detail=strings.NOT_UPDATED)
    return ServerResponse(msg=strings.SUCCESS)