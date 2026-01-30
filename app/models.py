from app.extenshions import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))
    role = db.Column(db.String(20), nullable=False)

    profile = db.relationship("Profile", backref="user", uselist=False)
    products = db.relationship("Product", backref="seller")


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    seller_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    reviews = db.relationship("Review", backref="product")


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default="pending")
    total = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    items = db.relationship("OrderItem", backref="order")


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
