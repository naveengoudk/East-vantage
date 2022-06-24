# importing requirements
from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

# importing local files
from routes import routes
from models import models
from schema import schema
from config.database import SessionLocal, engine

# creating table in sql database
models.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI()

#initiating database Dependency and connecting to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get request for all addresses

@app.get('/retrieve_all_address',response_model=List[schema.Address])
def retrieve_address(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return routes.get_Address(db=db, skip=skip, limit=limit)

# post request for addresses

@app.post('/add_new_address')
def add_new_address(address: schema.addAddress, db: Session = Depends(get_db)):
     return routes.add_Address_to_db(db=db, address=address)

# delete request for addresses

@app.delete('/delete_address_by_id/{id}')
def delete_address_by_id(id: int, db: Session = Depends(get_db)):
    return routes.delete_movie_details_by_id(db=db, id=id)   

# put request for addresses

@app.put('/update_address_details/{id}', response_model=schema.addAddress)
def update_address_details(id: int,details:schema.addAddress, db: Session = Depends(get_db)):
    return routes.update_movie_details(db=db,details=details,id=id)

# get all coordinates that are within a given distance of a given coordinate 
#    
@app.get("/get_all_coordinates_bydistance" ,response_model=List[schema.Address])
def get_cordinatesby_distance(latitude:float , longitude:float,distance:float, db:Session=Depends(get_db)):
    return routes.get_coordinates__bydistance(latitude, longitude,distance ,db)
