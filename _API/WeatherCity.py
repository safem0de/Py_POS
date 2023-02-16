import json
from Model import *

from flask_restful import Resource, abort, reqparse, marshal_with, fields
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

mycity = {
    1:{"name":"ชลบุรี",   "weather":"Hot",    "people":1500},
    2:{"name":"ระยอง",  "weather":"Rainy",  "people":2000},
    3:{"name":"กรุงเทพ", "weather":"Cold",   "people":5000},
}

city_add_args = reqparse.RequestParser()
city_add_args.add_argument("name",      type=str,   required=True,  help="Please input name")
city_add_args.add_argument("temp",      type=float, required=True,  help="Please input temperature")
city_add_args.add_argument("weather",   type=str,   required=True,  help="Please input weather")
city_add_args.add_argument("people",    type=int,   required=True,  help="Please input people")

resource_field = {
    "id": fields.Integer,
    "name": fields.String,
    "temp": fields.Float,
    "weather": fields.String,
    "people": fields.Integer,
}

engine = create_engine("sqlite:///_API/database.sqlite", echo=True)
Base.metadata.create_all(engine)

# conn = engine.connect()

Session = sessionmaker(engine, expire_on_commit=False)
session = Session()

def notFound(city_id):
    if city_id not in mycity:
        abort(404, message="Not Found Data")


class WeatherCity(Resource):

    @marshal_with(resource_field)
    def get(self, city_id):
        statement = select(City).filter_by(id = city_id)
        rows = session.execute(statement).one_or_none()
        print(type(rows))
        print(rows)
        
        return rows
    
    @marshal_with(resource_field)
    def post(self, city_id):
        args = city_add_args.parse_args()
        city = City(
            id = city_id,
            name = args["name"],
            temp = args["temp"],
            weather = args["weather"],
            people = args["people"],
        )
        try:
            session.add(city)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return city, 201
    