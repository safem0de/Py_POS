from flask import Flask
from flask_restful import Api

from WeatherCity import WeatherCity

app = Flask(__name__)
api = Api(app)

# call path
api.add_resource(WeatherCity, "/weather")


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)