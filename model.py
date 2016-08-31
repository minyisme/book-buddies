""" Models and database function for Goodreads Bookclub Generator"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ADD TABLES AND SUCH

def connect_to_db(app):   
    '''Create tables if none exist'''
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///goodreadsdb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://diana:hackbright@localhost:5432/goodreadsdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    # add if statements here
    db.create_all()

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Successfully connected to database"