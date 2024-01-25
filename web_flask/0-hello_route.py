#!/usr/bin/python3
"""Start a Flask application that 
    listens on 0.0.0.0 port=5000
    Routes: 
        /: To display 'Hello HBNB!'"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def display_hello_hbnb(text):
    """Display hello hbnb """
    return "Hello, HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
