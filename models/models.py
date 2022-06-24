from sqlalchemy import  Column, Float, Integer, String
from config.database import Base


# defining the model for table and coloums 
class AddressBook(Base):
    
    __tablename__ = "addressbook"
    
    # defining the coloumn
    id        =  Column(Integer, primary_key=True, index=True)
    street    =  Column(String,index=True)
    city      =  Column(String)
    state     =  Column(String)
    zipcode   =  Column(Integer)
    latitude  =  Column(Float)
    longitude =  Column(Float)


