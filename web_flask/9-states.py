#!/usr/bin/python3
"""Start a Flask app
    import Storage
    App listens on 0.0.0.0 port=5000
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def states_list():
    """Display states list"""
    states = storage.all("States")
    return render_template("9-states.html", states=states)

@app.route("/states/<id>", strict_slashes=False)
def states_id():
    """List states ID"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html")
        return render_template("9-states.html")

@app.teardown_appcontext
def teardown_context():
    """Close the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)