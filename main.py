from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h> Zuyo Hub SS winning?</h>"

@app.route("/api", methods=["GET"])

def test_api():
    if request.method == "GET":
        print("OOF FOUND SOME KID HACKING ON FORTNITE XD")
        return jsonify({"message": "succcess kiddo"})
if __name__ == "__main__":
    app.run(debug=True, port=80)
