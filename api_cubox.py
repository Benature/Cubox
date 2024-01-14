from flask import Flask, request, jsonify

from config import *

app = Flask(__name__)

from sender import *


@app.route("/cubox", methods=['POST'])
def cubox_func():
    data = request.get_json()
    r_new = cubox_new(data['url'])
    if r_new is None:
        return jsonify(dict(message="dulplicate url"))
    return jsonify(dict(code=200, message="Success"))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8642)
    # app.run(host="0.0.0.0", port=8642)
