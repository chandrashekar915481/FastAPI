from sqlalchemy import Float, Column, Integer, String
from db_handler import Base


class Addresses(Base):
    """
    This is a model class. which is having the address table structure with all the constraint
    """
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    address = Column(String(500), index=True, nullable=False)
    address_type = Column(String(100), index=True, nullable=False)
    pincode = Column(String, index=True, nullable=False)
    latitude = Column(Float, index=True, nullable=False)
    longitude = Column(Float, index=True, nullable=False)