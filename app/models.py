from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class Quote:
    def __init__(self, id, author, quote, url):
        self.id = id
        self.author = author
        self.quote = quote
        self.url = url

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))


    def __repr__(self):
        return f''