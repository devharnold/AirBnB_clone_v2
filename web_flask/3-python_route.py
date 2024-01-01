#!/usr/bin/python3
"""Start a Flask app
    Listens on 0.0.0.0 port=5000
    Routes
        /: Display hello hbnb
        /hbnb: Display hbnb
        /c/<text>: Display a 'c' text
        /python/<text>: Display a python text
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def display_hello_hbnb(text):
    """Display hello hbnb"""
    return "Hello, HBNB!"

@app.route("/hbnb", strict_slashes=False)
def display_hbnb(text):
    """display hbnb"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    """Display a C text"""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'

@app.route("/python/<text>", strict_slashes=False)
def display_python_text(text="is cool"):
    """Display a Python text"""
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)