from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def password(self, password):
        password_hash = generate_password_hash(password)
        self.password = password_hash
    

    def verify_password(self, password):
        return password(self.password, password)
    
    def __repr__(self):
        return f'User {self.username}'


class Tale:
    def __init__(self, id, author, quote, url):
        self.id = id
        self.author = author
        self.quote = quote
        self.url = url