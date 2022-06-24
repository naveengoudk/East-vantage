from pydantic import BaseModel


# define the schema for the request body
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

# define the schema for the response body for post request
class addAddress(BaseModel):
    street: str
    city: str
    state: str
    zip : int
    latitude : float
    longitude : float

    class Config:
        orm_mode = True