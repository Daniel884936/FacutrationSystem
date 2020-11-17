from sqlalchemy.orm import Session
from . import shemas, models

#--Products-------------------------------------------------------------------------------------------

def create_products(db: Session, product: shemas.ProductCreate):
    product_db:models.Porduct = models.Porduct(**product.dict())
    db.add(product_db)
    db.commit()
    db.refresh(product_db)
    

def get_all_products(db: Session):
    return db.query(models.Porduct).all()

def update_product(db: Session, product :shemas.ProductUpdate):
    product_to_update:models.Porduct  =  db.query(models.Porduct).filter(
        models.Porduct.idProduct==product.id).first()
    if not product_to_update:
        return False
    product_to_update.name = product.name
    product_to_update.price = product.price
    product_to_update.description = product.description
    product_to_update.stock = product.stock
    db.commit()
    return product_to_update
    
#--Invoice-------------------------------------------------------------------------------------------

