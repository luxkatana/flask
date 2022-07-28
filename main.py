from flask import Flask, jsonify
from flask_restful import Api, Resource

import os

app = Flask(__name__)
api = Api(app)
class something(Resource):
    def get(self):
        return jsonify({"message": "roblox, is that you?"})
@app.route('/')
def index():
    return jsonify({"Message": "Hello, World?"})

api.add_resource(something, "/")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
