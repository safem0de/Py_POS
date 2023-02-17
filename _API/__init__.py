from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# config
# python
# import secrets
# secrets.token_hex(20)

app.config["SECRET_KEY"] = 'e09281637cfcebf4b659a58d306ca2ee679cc838'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///_API/database.sqlite'

db = SQLAlchemy(app)

from _API import routes