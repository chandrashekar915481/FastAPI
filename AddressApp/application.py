from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Address Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_address_details', response_model=List[schema.Address])
def retrieve_all_address_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    addresses = crud.get_addresses(db=db, skip=skip, limit=limit)
    return addresses

@app.get('/all_address_details_within_range',response_model=List[schema.Address])
def all_address_details_within_range(latitude:float,longitude:float,distance:float, db: Session = Depends(get_db)):
    addr = crud.find_addresses(db=db,lat=latitude,lng=longitude,distance=distance)
    return addr

@app.post('/add_new_address', response_model=schema.AddressAdd)
def add_new_address(address: schema.AddressAdd, db: Session = Depends(get_db)):
    return crud.add_address_details_to_db(db=db,address=address)


@app.delete('/delete_address_by_id')
def delete_address_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_address_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_address_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_address_details', response_model=schema.Address)
def update_address_details(sl_id: int, update_param: schema.UpdateAddress, db: Session = Depends(get_db)):
    details = crud.get_address_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_address_details(db=db, details=update_param, sl_id=sl_id)