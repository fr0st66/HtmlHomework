from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    

class Recipe (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tital=db.Column(db.String (50))
    data = db.Column(db.String(50000))


