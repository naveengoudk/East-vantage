from fastapi import HTTPException
from sqlalchemy.orm import Session
import models.index
import schema.index
from math import radians, cos, sin, asin, sqrt

# GET address by id
def get_address_by_id(db:Session,id:int):
    return db.query(models.index.AddressBook).filter(models.index.AddressBook.id==id).first()

# GET all addresses
def get_Address(db,skip, limit):
    return db.query(models.index.AddressBook).offset(skip).limit(limit).all()

# POST address
def add_Address_to_db(db, address):
    if -90 <= address.latitude <=90 and -180 <= address.longitude <= 180:
        address_details = models.index.AddressBook(
            street=address.street,
            city=address.city,
            state=address.state,
            zip=address.zip,
            latitude=address.latitude,
            longitude=address.longitude
        )
        db.add(address_details)
        db.commit()
        db.refresh(address_details)
        return models.index.AddressBook(**address.dict())
    
    raise HTTPException(status_code=400 , detail=f"Invalid coordinates")

# UPDATE address
def update_movie_details(db: Session, id: int, details: schema.index.Address):
    address = get_address_by_id(id=id,db=db)
    if not address:
        raise HTTPException(status_code=404, detail=f"No record found to update")
    else:
        if -90 <= details.latitude <=90 and -180 <= details.longitude <= 180:
            db.query(models.index.AddressBook).filter(models.index.AddressBook.id == id).update(vars(details))
            db.commit()
            return db.query(models.index.AddressBook).filter(models.index.AddressBook.id == id).first()
        else:
            raise HTTPException(status_code=400 , detail=f"Invalid coordinates")

# DELETE address   
def delete_movie_details_by_id(db: Session, id: int):
    address = get_address_by_id(id=id,db=db)
    if not address:
        raise HTTPException(status_code=404, detail=f"No record found to delete")
    try:
        db.query(models.index.AddressBook).filter(models.index.AddressBook.id == id).delete()
        db.commit()
        return {"delete status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
  
# GET coordinates by distance
def distance(lat1, lat2, lon1, lon2):
	
	lon1 = radians(lon1)
	lon2 = radians(lon2)
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	
	# Haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

	c = 2 * asin(sqrt(a))
	
	# Radius of earth in kilometers
	r = 6371
	
	# calculate the result
	return(c * r)
	

def get_coordinates__bydistance(lat,long,dist,db:Session):
    if -90 <= lat <=90 and -180 <= long <= 180:
        addresses = db.query(models.index.AddressBook).all()
        address_btw_coordinates=[]
        for items in addresses:
            distance_from_coordinates = distance(lat , items.latitude , long,items.longitude)
            if distance_from_coordinates <= dist:
                address_btw_coordinates.append(items)
        return address_btw_coordinates
    raise HTTPException(status_code=400 , detail=f"Invalid coordinates")



	






