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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text='is cool'):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
