#!/usr/bin/python3
"""flask app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', _slashes=False)
def hello_hbnb():
    """ Hello HBNB """
    return 'Hello HBNB!'


@app.route("/hbnb", _slashes=False)
def hello_hbnb():
    """ Hello HBNB """
    return 'HBNB'


@app.route("/c/<text>", _slashes=False)
def c():
    """ Hello HBNB """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route("/python/(<text>)", _slashes=False)
def python():
	""" Hello HBNB """
	text = text.replace('_', ' ')
	return 'Python {}'.format(text)

if "__main__" == __name__:
    app.run(host='0.0.0.0', port=5000)