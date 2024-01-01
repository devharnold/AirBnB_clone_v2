#!/usr/bin/python3
"""Start a Flask app
    import models, storage
    App listens from 0.0.0.0 port=5000
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """List states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_context(exception):
    """Close the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)