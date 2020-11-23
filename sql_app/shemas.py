from pydantic import BaseModel
from datetime import datetime
from typing import List

class ServerResponse:
    def __init__(self, ok:bool = True, msg:str = '', data = '' ):
       self.ok = ok
       self.msg = msg
       self.data = data
    ok:bool 
    msg:str 
    data = ''

class ProductBase(BaseModel):
    name:str
    description:str
    price:float
    stock:int
    
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    id:int

class Invoice_DetailBase(BaseModel):
    price:float
    quantity:int
    idProduct:int
    
class InvoiceBase(BaseModel):
    client_name:str
    description:str
    rnc:str
    date:datetime
    pass

class InvoiceCreate(InvoiceBase):
    invoice_details: List[Invoice_DetailBase] = []