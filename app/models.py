from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


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
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
                
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    
    def __repr__(self):
        return f'User {self.username}'