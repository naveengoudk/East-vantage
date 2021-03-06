# importing required modules and files
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import models
from schema import schema
from calculateDistance import distance
import logging


# coordinates are valid if -90 <= latitude <=90 and -180 <= longitude <= 180


#implementing logging for releasing logs to file
logging.basicConfig(filename='logs/logs.log', level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.info('Logging started') 

# function for getting address by id database
def get_address_by_id( db : Session , id : int):
    return db.query(models.AddressBook).filter(models.AddressBook.id == id).first() 

# function for getting all address from database
def get_Address(db , skip , limit):
    logger.info('Getting all addresses')
    return db.query(models.AddressBook).offset(skip).limit(limit).all()

# function for posting address to database
def add_Address_to_db(db, address):
    logger.info('validating coordinates')
    # posting to database if coordinates are valid
    if -90 <= address.latitude <=90 and -180 <= address.longitude <= 180:
        new_address = address_details =models.AddressBook(
            street = address.street,
            city = address.city,
            state = address.state,
            zipcode = address.zipcode,
            latitude = address.latitude,
            longitude = address.longitude
        )
        db.add(address_details)
        db.commit()
        db.refresh(address_details)
        logger.info('coordinates validated')
        logger.info('Address added to database')
        return new_address
    #rasing exception if coordinates are not valid
    logger.info('Invalid coordinates')
    raise HTTPException(status_code=400 , detail=f"Invalid coordinates") 

# function for updating address by id in database
def update_movie_details(db: Session, id: int, details: schema.Address):
    # get address by id from path variable
    logger.info('Getting address by id')
    address = get_address_by_id(id = id , db = db)
    #rasing exception if id is not found in database
    if not address:
        logger.info('Address not found')
        raise HTTPException(status_code=404, detail=f"No record found to update") 
    else:
        logger.info('validating coordinates')
        # updating if coordinates are valid
        if -90 <= details.latitude <=90 and -180 <= details.longitude <= 180:
            db.query(models.AddressBook).filter(models.AddressBook.id == id).update(vars(details))
            db.commit()
            logger.info("coordinates validated")
            logger.info('Address updated')
            return db.query(models.AddressBook).filter(models.AddressBook.id == id).first()
        else:
            #rasing exception if coordinates are not valid
            logger.info('Invalid coordinates')
            raise HTTPException(status_code=400 , detail=f"Invalid coordinates") 

# function for deleting address by id in database
def delete_movie_details_by_id(db: Session, id: int):
    # get address by id from path variable
    logger.info('Getting address by id')
    address = get_address_by_id( id = id,db = db)
    #rasing exception if id is not found in database
    if not address:
        logger.info('Address not found')
        raise HTTPException(status_code=404, detail=f"No record found to delete")
    try:
        db.query(models.AddressBook).filter(models.AddressBook.id == id).delete()
        db.commit()
        logger.info('Address deleted')
        return {"delete status": "success"}
    except Exception as e:
        #rasing exception if address is not deleted
        logger.info('Address not deleted')
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
  
# function for getting all coordinates with in a given distance and coordinates	
def get_coordinates__bydistance(lat , long , dist , db: Session):
    # checking if coordinates are valid
    logger.info('validating coordinates')
    if -90 <= lat <=90 and -180 <= long <= 180:
        logger.info("coordinates validated")
        logger.info('Getting all coordinates with in a given distance') 
        addresses = db.query(models.AddressBook).all()
        address_btw_coordinates=[]
        for items in addresses:
            # for each coordinate(lat,long) in database calculating the distance between given coordinates by using haversine formula 
            distance_from_coordinates = distance.distance(lat , items.latitude , long,items.longitude)
            if distance_from_coordinates <= dist:
                # if distance is less than given distance append the coordinates to address_btw_coordinates list
                address_btw_coordinates.append(items)
        logger.info('coordinates found')
        return address_btw_coordinates

    #rasing exception if coordinates are not valid
    logger.info('Invalid coordinates')
    raise HTTPException(status_code=400 , detail=f"Invalid coordinates")



	






