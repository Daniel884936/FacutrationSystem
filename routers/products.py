from fastapi import APIRouter, Depends, HTTPException
from dependencies.database import get_db
from sqlalchemy.orm import Session
from starlette import status
from sql_app import shemas, crud


router = APIRouter()

@router.post('/create')
def create_product(product: shemas.ProductCreate ,db: Session  = Depends(get_db)):
    crud.create_products(db, product)
    return{'detail':'created'}


@router.get('/get')
def get_all_products(db: Session  = Depends(get_db)):
    products = crud.get_all_products(db)
    if not products:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                            detail='products not found')
    return{'products': products}


@router.put('/update')
def update_prodcut(product:shemas.ProductUpdate,db: Session  = Depends(get_db)):
    product_updated =  crud.update_product(db,product)
    if not product_updated:
       raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                           detail='cannot updated, product not found')
    return{'detail': 'updated'}