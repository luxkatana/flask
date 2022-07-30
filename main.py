from flask import Flask, jsonify, request
from random import randint
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(host="containers-us-west-86.railway.app", database="railway", user="postgres", password="WbulsHpSTTKWk9spS9PU", port=7551)
cursor = conn.cursor()
@app.route("/")
def hello_world():
    return "<h> Zuyo Hub SS winning?</h>"
# test msg
@app.route("/api", methods=["GET"])
def api():
    if request.method == "GET":
        js = request.get_json()
        params = request.args
        print(params)
        print(params)
        if params != None:
            try:
                robloxID = params["robloxID"]
            except KeyError:
                return jsonify({"error": "missing robloxID key"})
            cursor.execute("select * from whitelisted where robloxid={};".format(robloxID))
            d = cursor.fetchall()
            if d != []:
                return jsonify({"status": "whitelisted"})
            else:
                cursor.execute("select * from blacklisted where robloxID={};".format(robloxID))
                d = cursor.fetchall()
                if d != []:
                    return jsonify({"status": "blacklisted"})
                else:
                    return jsonify({"status": "nonwl"})
                
if __name__ == "__main__":
    app.run(debug=True, port=80)
    # conn = psycopg2.connect()