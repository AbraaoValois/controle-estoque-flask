from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime  # Import necessário para a data da compra

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(20))
    purchases = db.relationship('Purchase', backref='client', lazy=True)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    is_paid = db.Column(db.Boolean, default=False)
    data = db.Column(db.Date, default=datetime.utcnow)  # Novo campo para a data da compra
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    unit_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

