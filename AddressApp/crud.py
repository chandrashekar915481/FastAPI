from sqlalchemy.orm import Session
from sqlalchemy import false, true
import model
import schema
import math


def get_address_by_id(db: Session, sl_id: int):
    """
    This method will return single address details based on id
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: data row if exist else None
    """
    return db.query(model.Addresses).filter(model.Addresses.id == sl_id).first()


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return all address details which are present in database
    :param db: database session object
    :param skip: the number of rows to skip before including them in the result
    :param limit: to specify the maximum number of results to be returned
    :return: all the row from database
    """
    return db.query(model.Addresses).offset(skip).limit(limit).all()


def add_address_details_to_db(db: Session, address: schema.AddressAdd):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    :param db: database session object
    :param address: Object of class schema.AddressAdd
    :return: a dictionary object of the record which has inserted
    """
    ad_details = model.Addresses(
        address=address.address,
        address_type=address.address_type,
        pincode=address.pincode,
        latitude=address.latitude,
        longitude=address.longitude
    )
    db.add(ad_details)
    db.commit()
    db.refresh(ad_details)
    return model.Addresses(**address.dict())


def update_address_details(db: Session, sl_id: int, details: schema.UpdateAddress):
    """
    this method will update the database
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :param details: Object of class schema.UpdateAddress
    :return: updated address record
    """
    db.query(model.Addresses).filter(model.Addresses.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Addresses).filter(model.Addresses.id == sl_id).first()


def delete_address_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: None
    """
    try:
        db.query(model.Addresses).filter(model.Addresses.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)

def within_range(lat1,lat2,lng1,lng2,dis):
    org_dis = math.sqrt(math.pow(69.1 * (lat2 - lat1), 2) + math.pow(69.1 * (lng1 - lng2) * math.cos(lat2 / 57.3), 2))
    if org_dis<dis:
        return true
    else:
        return false

def find_addresses(db: Session,lat:float,lng:float,distance:float):
    try:
        all_address = db.query(model.Addresses).all()
        res=[]
        for ad in all_address:
            a=within_range(lat,ad.latitude,lng,ad.longitude,distance)
            if a==true:
                res.append(ad)
        return res
    except Exception as e:
        raise Exception(e)
