from typing import Optional, Union

from dotenv import dotenv_values
from flask import Flask, jsonify, request, Response

from controllers import operation

app = Flask(__name__)


def get_port() -> Union[str, None, int]:
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5000


@app.route("/")
def hello() -> str:
    return "Hello, Welcome to my server"

@app.route("/author")
def author() -> Response:
    authorr = {
        "name": "Luba",
        "course": 3,
        "age": 20,
    }
    return jsonify(authorr)

@app.route("/sum")
def runner() -> Response:
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})


if __name__ == "__main__":
    app.run(debug=True, port=get_port())
