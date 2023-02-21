from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

import crud as c
import schemas as s
import models as m
from database import SessionLocal, engine

m.Base.metadata.create_all(bind=engine)
# https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_2_3

app = FastAPI()

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


@app.get("/")
def read_root():
    return {"Hello": "Test"}


@app.post("/users/", response_model=s.User, tags=["users"])
def create_user(user: s.UserCreate, db: Session = Depends(get_db)):
    db_user = c.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return c.create_user(db=db, user=user)


@app.get("/users/", response_model=list[s.User], tags=["users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = c.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=s.User, tags=["users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = c.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=s.Item, tags=["users"])
def create_item_for_user(
    user_id: int, item: s.ItemCreate, db: Session = Depends(get_db)
):
    return c.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[s.Item], tags=["items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = c.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/products/", response_model=list[s.Product], tags=["products"])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = c.get_products(db, skip=skip, limit=limit)
    return products


@app.post("/units/{unit_id}/products", response_model=s.Product, tags=["products"])
def create_product(unit_id: int, product: s.ProductCreate, db: Session = Depends(get_db)):
    return c.create_product(db=db, product=product, unit_id=unit_id)


@app.get("/units/", response_model=list[s.Unit], tags=["units"])
def read_units(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    units = c.get_units(db, skip=skip, limit=limit)
    return units


@app.post("/units/", response_model=s.Unit, tags=["units"])
def create_unit(unit: s.UnitCreate, db: Session = Depends(get_db)):
    db_unit = c.get_unit_by_name(db, name=unit.name)
    if db_unit:
        raise HTTPException(status_code=400, detail="unit already registered")
    return c.create_unit(db=db, unit=unit)