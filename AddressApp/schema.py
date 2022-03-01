from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    address: str
    pincode: str
    latitude: float
    longitude:float



class AddressAdd(AddressBase):
    # Optional[str] is just a shorthand or alias for Union[str, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    address_type: Optional[str] = None

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class Address(AddressAdd):
    id: int

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class UpdateAddress(BaseModel):
    # Optional[str] is just a shorthand or alias for Union[str, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    address_type: Optional[str] = None
    address: str
    pincode: str
    latitude: float
    longitude: float

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True