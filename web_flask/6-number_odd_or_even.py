#!/usr/bin/python3

from flask import Flask, render_template

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

@app.route("/python/<text>", strict_slashes=False)
def display_python_text(text="is cool"):
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'

@app.route("/number/<n>", strict_slashes=False)
def diplay_n_number(n):
    return f'{n} is a number'

@app.route("/number_template/<n>", strict_slashes=False)
def display_template(n):
    return render_template('5-number.html', n=n)

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def display_template(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)