from flask import Flask, jsonify
from flask_restful import Api, Resource
import psycopg2
import os
import dotenv
app = Flask(__name__)
api = Api(app)
dotenv.load_dotenv()
DBHOST = os.environ["DBHOST"]
DBNAME = os.environ["DBNAME"]
DBUSER = os.environ["DBUSER"]
DBPASSWORD = os.environ["DBPASSWORD"]
DBPORT = os.environ["DBPORT"]
connection = psycopg2.connect(database=DBNAME, user=DBUSER, password=DBPASSWORD, host=DBHOST, port=DBPORT)
cursor = connection.cursor()
class something(Resource):
    def get(self, data):
        try:
            data["robloxID"]
        except KeyError as e:
            return jsonify({"error": "missing robloxID"})
        cursor.execute("select * from whitelisted where robloxID=?;", (data["robloxID"],))
        d = cursor.fetchall()
        return jsonify({"status": d[0]["robloxid"]})

@app.route('/')
def index():
    return jsonify({"Message": "Hello, World?"})

api.add_resource(something, "/")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
