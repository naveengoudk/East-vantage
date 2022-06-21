from sqlalchemy import  Column, Float, Integer, String
from config.database import Base


class AddressBook(Base):
    __tablename__ = "addressbook"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String,index=True)
    city = Column(String)
    state = Column(String)
    zip = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)


