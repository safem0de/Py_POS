from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    product_name: str
    product_code: str
    product_price: float
    unit_id: int


class ProductCreate(ProductBase):
    product_cost: float


class Product(ProductBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
