from flask import Flask, Response, jsonify, make_response, request
from flask_cors import CORS

# App Setup
app = Flask(__name__)
CORS(app)

# ROutes
@app.route("/test", methods=["POST"])
def test():
    test_dict = {"message": "Hello, World!"}

    return make_response(jsonify(test_dict), 200)
