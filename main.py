from flask import Flask, jsonify, request
from random import randint
import psycopg2

app = Flask(__name__)
conn = None
@app.route("/")
def hello_world():
    return "<h> Zuyo Hub SS winning?</h>"
# test msg
@app.route("/api", methods=["POST"])
def test_api():
    if request.method == "POST":
        data = request.json
        print(data)
        return jsonify({"status": "data: {}".format(data[0])})

if __name__ == "__main__":
    app.run(debug=True, port=80)
    # conn = psycopg2.connect()