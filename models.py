from . import db
#Write all tables and attributes here
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
     __tablename__ = 'Book'
     title = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)

     def __repr__(self):
        return "<Title: {}>".format(self.title)
     
class Patron(db.Model):
     __tablename__ = 'Patron'
     title = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)

     def __repr__(self):
        return "<Title: {}>".format(self.title)
     
class Librarian(db.Model):
     __tablename__ = 'Librarian'
     title = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)

     def __repr__(self):
        return "<Title: {}>".format(self.title)
     
class Author(db.Model):
     __tablename__ = 'Author'
     author_firstName = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
     def __repr__(self):
        return "<Title: {}>".format(self.author_firstName)
     
#Write a class for transaction as well (Sanjana):
class Transaction(db.Model):
     __tablename__ = 'Transaction'
     transaction_id = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
     def __repr__(self):
        return "<Title: {}>".format(self.transaction_id)