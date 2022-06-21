from pydantic import BaseModel

class Address(BaseModel):
    id:int
    street: str
    city: str
    state: str
    zip : int
    latitude : float
    longitude : float

    class Config:
        orm_mode = True

class addAddress(BaseModel):
    street: str
    city: str
    state: str
    zip : int
    latitude : float
    longitude : float

    class Config:
        orm_mode = True