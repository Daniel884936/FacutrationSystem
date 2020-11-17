from pydantic import BaseModel

class ProductBase(BaseModel):
    name:str
    description:str
    price:float
    stock:int
    
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    id:int