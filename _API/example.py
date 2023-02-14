# https://prisan6046.medium.com/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-api-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-python-57262e80e169
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home(): 
   arr = {
      "fname" : "Prisan",
      "lname" : "Pimprasan",
      "nickname" : "Big"
   } 
   return jsonify(arr)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)