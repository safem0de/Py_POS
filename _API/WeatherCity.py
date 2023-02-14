from flask_restful import Resource, abort

mycity = {
    1:{"name":"ชลบุรี",   "weather":"Hot",    "people":1500},
    2:{"name":"ระยอง",  "weather":"Rainy",  "people":2000},
    3:{"name":"กรุงเทพ", "weather":"Cold",   "people":5000},
}

def notFound(city_id):
    if city_id not in mycity:
        abort(404, message="Not Found Data")

class WeatherCity(Resource):
    # def get(self):
    #     return mycity

    def get(self, city_id):
        notFound(city_id)
        return mycity[city_id]
    
    def post(self, name):
        return {"data":"Create resource = " + name}
    