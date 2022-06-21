from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import routes.routes
import models.index
import schema.index
from config.database import SessionLocal, engine

models.index.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_address',response_model=List[schema.index.Address])
def retrieve_address(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return routes.routes.get_Address(db=db, skip=skip, limit=limit)
   
@app.post('/add_new_address')
def add_new_address(address: schema.index.addAddress, db: Session = Depends(get_db)):
     return routes.routes.add_Address_to_db(db=db, address=address)
    
@app.delete('/delete_address_by_id')
def delete_address_by_id(id: int, db: Session = Depends(get_db)):
    return routes.routes.delete_movie_details_by_id(db=db, id=id)   

@app.put('/update_address_details', response_model=schema.index.addAddress)
def update_address_details(id: int,details:schema.index.addAddress, db: Session = Depends(get_db)):
    return routes.routes.update_movie_details(db=db,details=details,id=id)
   
@app.get("/get_all_coordinates_bydistance" ,response_model=List[schema.index.Address])
def get_cordinatesby_distance(latitude:float , longitude:float,distance:float, db:Session=Depends(get_db)):
    return routes.routes.get_coordinates__bydistance(latitude, longitude,distance ,db)

