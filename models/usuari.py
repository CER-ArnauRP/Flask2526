
from flask_login import UserMixin
from extensions import db

class Usuari(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom_usuari = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    hash_password = db.Column(db.String(150), unique=True)