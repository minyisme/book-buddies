from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, json, jsonify
from flask_debugtoolbar import DebugToolbarExtension
# add tables from model.py when ready
from model import connect_to_db, db
import os


app = Flask(__name__)

app.secret_key = "itsasecret"

# raises error if you use an undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")













if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()