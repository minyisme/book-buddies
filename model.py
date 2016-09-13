""" Models and database function for Goodreads Bookclub Generator"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# active goodreads users class
class User(db.Model):
    """A goodreads user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    account_link = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(50), nullable=True)


    def __repr__(self):
        """Provide helpful representation when printed to console"""

        return "<User id=%s location=%s acct_link=%s>" % (self.user_id,
            self.location, self.account_link)


# users can view and join bookclubs to be a part of
class Bookclub(db.Model):
    """A book buddies bookclub user can join, has shelves of its own"""

    __tablename__ = "bookclubs"

    bookclub_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    description = db.Column(db.String(250), nullable=True)
    title = db.Column(db.String(100), nullable=True)
    read_shelf = db.Column(db.String(50), nullable=True)
    current_shelf = db.Column(db.String(50), nullable=True)
    recommended_shelf = db.Column(db.String(50), nullable=True)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Bookclub_id=%s title=%s>" % (self.bookclub_id, self.title))


# a connection between user and bookclub constitutes membership
class Membership(db.Model):
    """A user's membership in a bookclub, an association table"""

    __tablename__ = "memberships"

    membership_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    bookclub_id = db.Column(db.Integer, db.ForeignKey('bookclubs.bookclub_id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)

    # define relationship to User table
    user = db.relationship("User", backref=db.backref("memberships"))

    # define relationship to Bookclub table
    bookclub = db.relationship("Bookclub", backref=db.backref("memberships"))


# a shelf is a category of books within a bookclub that indicate its users tastes
class Shelf(db.Model):
    """A shelf within a bookclub"""

    __tablename__ = "shelves"

    shelf_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    bookclub_id = db.Column(db.Integer, db.ForeignKey('bookclubs.bookclub_id'), nullable=True)
    # 3 categories of shelf: read, current, recommended
    category = db.Column(db.String(11), nullable=True)

    # define relationship to Bookclub table
    bookclub = db.relationship("Bookclub", backref=db.backref("shelves"))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Shelf_id=%s bookclub_id=%s category=%s>" % (self.shelf_id,
            self.bookclub_id, self.category))


# a book is a novel that is of interest to the users and placed on a shelf
class Book(db.Model):
    """A book within a shelf, a book that is part of a bookclub's shelf"""

    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_link = db.Column(db.String(100), nullable=True)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return ("<Book_id=%s book_link=%s>" % (self.book_id, self.book_link))


# a book and shelf have a connection of belonging there based on taste
class Belonging(db.Model):
    """An association table between a book and a shelf"""

    __tablename__ = "belongings"

    belonging_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=True)
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelves.shelf_id'), nullable=True)

    # define relationship to Book table
    book = db.relationship("Book", backref=db.backref("belongings"))

    # define relationship to Shelf table
    shelf = db.relationship("Shelf", backref=db.backref("belongings"))


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