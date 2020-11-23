from fastapi import APIRouter, Depends, HTTPException
from sql_app import shemas, crud
from sqlalchemy.orm import Session
from sql_app.shemas import ServerResponse 
from dependencies.database import get_db
from resources import strings
from starlette import status

router = APIRouter()
#TODO
@router.post('/create')
def create(invoice:shemas.InvoiceCreate, db:Session = Depends(get_db)):
    #begind calculations
    sub_total:float = 0 
    for item in invoice.invoice_details:
        price_per_quality:float = item.price * item.quantity
        sub_total= sub_total +price_per_quality
    itbts:float = 0.18
    total:float = sub_total - sub_total *itbts
    #end
    crud.create_invoice(db,invoice,sub_total,total)
    return ServerResponse(msg=strings.SUCCESS)      


@router.get('/getall')
def get_all(db:Session = Depends(get_db)):
    invioices = crud.get_all(db)
    if not invioices:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.INVOICE_NOT_FOUND)
    return ServerResponse(msg=strings.SUCCESS, data=invioices)

@router.get('/getInvoiceDetails/{id_invoice}')
def funcname(id_invoice:int, db:Session = Depends(get_db)):
    invoice_details = crud.get_invoice_datials_from_invoice(db,id_invoice)
    if not invoice_details:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.INVOICE_NOT_FOUND)
    return ServerResponse(msg=strings.SUCCESS, data=invoice_details)


                                                                                                                    