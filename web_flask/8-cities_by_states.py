#!/usr/bin/python3
""" 
Start a Flask app
Import models, storage
App listens on 0.0.0.0 port=50000
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_list():
    """List cities"""
    states = storage.all("States")
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown_context():
    """Close the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)