from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, ForeignKey

class Invoice(Base):
    __tablename__ = 'invoices'
    
    idInvoice = Column(Integer, primary_key = True, index= True)
    client_name = Column(String)
    description = Column(String)
    rnc = Column(Integer)
    sub_total = Column(Float)
    total = Column(Float)
    date = Column(DateTime)

class Porduct(Base):
    __tablename__='products'
    idProduct = Column(Integer, index=True, primary_key = True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    
class Invoice_Detail(Base):
    __tablename__= 'invoice_details'
    
    idInvoice_detail = Column(Integer, index=True, primary_key = True)
    price = Column(Float)
    quantity = Column(Integer)
    idInvoice  = Column(Integer, ForeignKey('invoices.idInvoice'))
    idProduct  = Column(Integer, ForeignKey('products.idProduct'))