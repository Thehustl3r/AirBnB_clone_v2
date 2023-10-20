#!/usr/bin/python3
""" this module we will be dealing with intro to Flask """
from flask import render_template, request, Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello(name=None):
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbhb(name=None):
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
