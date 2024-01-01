#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def display_hello_hbnb(text):
    return "Hello, HBNB!"

@app.route("/hbnb", strict_slashes=False)
def display_hbnb(text):
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def display_c_text(text):
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)