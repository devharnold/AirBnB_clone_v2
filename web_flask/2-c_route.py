#!/usr/bin/python3
"""Start a Flask app
    Listens on 0.0.0.0 port=5000
    Routes
        /: Display hello hbnb
        /hbnb: Display hbnb
        /c/<text>: Display a 'c' text
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def display_hello_hbnb(text):
    """display hello hbnb"""
    return "Hello, HBNB!"

@app.route("/hbnb", strict_slashes=False)
def display_hbnb(text):
    """display hbnb"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    """Display a formatted text"""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)