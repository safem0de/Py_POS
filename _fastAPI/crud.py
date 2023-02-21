from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate, unit_id:int):
    db_product = models.Product(
        **product.dict(),
        product_unit_id = unit_id
        )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_units(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Unit).offset(skip).limit(limit).all()


def get_unit_by_name(db: Session, name: str):
    return db.query(models.Unit).filter(models.Unit.name == name).first()


def create_unit(db: Session, unit: schemas.UnitCreate):
    db_unit = models.Unit(name = unit.name)
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit