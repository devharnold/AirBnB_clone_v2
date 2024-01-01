#!/usr/bin/python3
"""Start a Flask app
    Listens on 0.0.0.0 port=5000
    routes: /:Display 'Hello HBNB!'
            /hnbb: Display hbnb
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)