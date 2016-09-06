from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, json, jsonify
from flask_debugtoolbar import DebugToolbarExtension
# add tables from model.py when ready
from model import connect_to_db, db
import os
from rauth.service import OAuth1Service, OAuth1Session
import urllib2
import requests

CONSUMER_KEY = os.environ['GOODREADS_KEY']
CONSUMER_SECRET = os.environ['GOODREADS_SECRET']


def authorize_user():
    """This uses goodreads oauth to authorize user into app."""   
    goodreads = OAuth1Service(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        name='goodreads',
        request_token_url='http://www.goodreads.com/oauth/request_token',
        authorize_url='http://www.goodreads.com/oauth/authorize',
        access_token_url='http://www.goodreads.com/oauth/access_token',
        base_url='http://www.goodreads.com/'
        )

    request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

    authorize_url = goodreads.get_authorize_url(request_token)
    print 'Visit this URL in your browser: ' + authorize_url
    accepted = 'n'
    while accepted.lower() == 'n':
        # you need to access the authorize_link via a browser,
        # and proceed to manually authorize the consumer
        accepted = raw_input('Have you authorized me? (y/n) ')
    print accepted

def user_info_by_id(user_id):
    """Uses GR's user.show to get user info, including location, by id"""
    url = "https://www.goodreads.com/user/show/%s.xml" %(user_id)

    results = requests.get(url, data={"key": CONSUMER_KEY, "id": user_id})

    return results.text


























app = Flask(__name__)

app.secret_key = "itsasecret"

# raises error if you use an undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")













# if __name__ == "__main__":
#     # We have to set debug=True here, since it has to be True at the point
#     # that we invoke the DebugToolbarExtension
#     app.debug = True

#     connect_to_db(app)

#     # Use the DebugToolbar
#     DebugToolbarExtension(app)

#     app.run()