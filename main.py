from flask import Flask, jsonify, request
from random import randint
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h> Zuyo Hub SS winning?</h>"
# test msg
@app.route("/api", methods=["POST"])
def test_api():
    if request.method == "POST":
        print("The data is: {}".format(request.data.decode()))
        return jsonify({"randNum": randint(1, 100)})

if __name__ == "__main__":
    app.run(debug=True, port=80)

