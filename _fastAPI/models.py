from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


# class Unit(Base):
#     __tablename__ = "units"

#     id = Column(Integer, primary_key=True, index=True)
#     unit_name = Column(String, unique=True)

#     products = relationship("Product", back_populates="unit")

# class Product(Base):
#     __tablename__ = "products"

#     id = Column(Integer, primary_key=True, index=True)
#     product_name = Column(String)
#     product_code = Column(String)
#     product_price = Column(float)
#     product_cost = Column(float)
#     unit_id = Column(Integer, ForeignKey("units.id"))
#     is_active = Column(Boolean, default=True)

#     unit = relationship("", back_populates="")