from sqlalchemy.orm import Session

import models as m
import schemas as s


def get_user(db: Session, user_id: int):
    return db.query(m.User).filter(m.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(m.User).filter(m.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(m.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: s.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = m.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(m.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: s.ItemCreate, user_id: int):
    db_item = m.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(m.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: s.ProductCreate, unit_id:int):
    db_product = m.Product(
        **product.dict(),
        product_unit_id = unit_id
        )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_units(db: Session, skip: int = 0, limit: int = 100):
    return db.query(m.Unit).offset(skip).limit(limit).all()


def get_unit_by_name(db: Session, name: str):
    return db.query(m.Unit).filter(m.Unit.name == name).first()


def create_unit(db: Session, unit: s.UnitCreate):
    db_unit = m.Unit(name = unit.name)
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit