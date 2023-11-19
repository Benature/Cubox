from flask import Flask, request, jsonify

from config import *

app = Flask(__name__)

from sender import *


@app.route("/cubox", methods=['POST'])
def cubox_func():
    data = request.get_json()
    cubox_new(data['url'])
    # Process the JSON data here
    # ...
    return jsonify({"message": "Success"})


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8642)
