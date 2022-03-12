from . import db
from flask_login import UserMixin

class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    bday = db.Column(db.DateTime(timezone=True))
