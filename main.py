from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h> Zuyo Hub SS winning?</h>"
# test msg
@app.route("/api", methods=["POST"])
def test_api():
    if request.method == "POST":
        print(request.data)

        return jsonify({"data responded:": request.data["data"]})

if __name__ == "__main__":
    app.run(debug=True, port=80)
