#!/usr/bin/python3
"""Start a Flask app
    Listens on 0.0.0.0 port=5000
    Routes
        /: Display hello hbnb
        /hbnb: Display hbnb
        /c/<text>: Display a 'c' text
        /number/<n>: Display a number
        /number_template/<n>: Display a number template
        /number_odd_or_even/<n>: Display an odd_or_even number
"""
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.trim_blocks = True

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
    """display a C text"""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'

@app.route("/python/<text>", strict_slashes=False)
def display_python_text(text="is cool"):
    """display a python text"""
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'

@app.route("/number/<n>", strict_slashes=False)
def diplay_n_number(n):
    """display a number"""
    return f'{n} is a number'

@app.route("/number_template/<n>", strict_slashes=False)
def display_template(n):
    """display a HTML page only if an integer"""
    return render_template('5-number.html', n=n)

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def display_template(n):
    """display a odd or even number, only if an integer"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)