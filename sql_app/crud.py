from sqlalchemy.orm import Session
from . import shemas, models
from typing import List

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
#TODO
def create_invoice(db:Session,invoice:shemas.InvoiceCreate, sub_total:float, total:float):    
    invoce_db:models.Invoice = models.Invoice(
        client_name= invoice.client_name,
        description= invoice.description, 
        rnc= invoice.rnc,
        sub_total= sub_total,
        total = total,
        date = invoice.date
    )
    db.add(invoce_db)
    db.commit()
    db.refresh(invoce_db)
    create_invoice_details(db,invoce_db.idInvoice,invoice.invoice_details)

#TODO
def create_invoice_details(db:Session, id_invoice:int, invoice_details:List[shemas.Invoice_DetailBase]):     
    invoice_details_db:List[models.Invoice_Detail] = []
    for item in invoice_details:
        invoice_details_db.append(models.Invoice_Detail(**item.dict(), idInvoice = id_invoice))
    db.add_all(invoice_details_db)
    db.commit()
    
def get_all(db:Session):
    return db.query(models.Invoice).all()
    pass

def get_invoice_datials_from_invoice(db:Session, id_invoce:int):
    return db.query(models.Invoice_Detail).filter(
        models.Invoice_Detail.idInvoice ==id_invoce).all()