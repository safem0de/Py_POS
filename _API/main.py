from flask import Flask
from flask_restful import Api

from sqlalchemy import create_engine

from Model import *

from WeatherCity import WeatherCity
from HelloWorld import HelloWorld

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'

# db = SQLAlchemy(app)
api = Api(app)

# class CityModel(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(100), nullable=False)
#    temp = db.Column(db.String(100), nullable=False)
#    weather = db.Column(db.String(100), nullable=False)
#    people = db.Column(db.String(100), nullable=False)

#    def __repr__(self):
#       return f"City(name={self.name},temp={self.temp},weahter={self.weather},people={self.people})"

# with app.app_context():
#    # https://stackoverflow.com/questions/34122949/working-outside-of-application-context-flask
#    # Yohanes Getient
#    db.create_all()


engine = create_engine("sqlite:///_API/database.sqlite", echo=True)
Base.metadata.create_all(engine)

# call path
api.add_resource(HelloWorld, "/", "/hello")
api.add_resource(WeatherCity, "/weather/<int:city_id>")

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)