from math import inf
from flask_login import UserMixin
from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import DECIMAL
db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(100), unique=False , nullable=False)
    user_handle = db.Column(db.String(100), unique=True , nullable=False)
    user_password = db.Column(db.String(100) , nullable=False)
    user_email = db.Column(db.String(100) , nullable=False)
    user_role = db.Column(db.Numeric())

    def get_id(self):
        return (self.user_id)

class Proffessional(db.Model):
    __tablename__ = 'proffessional'
    proffessional_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    proffessional_user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    proffessional_company_name = db.Column(db.String(100))
    proffessional_date_created = db.Column(db.DateTime, default=dt.now())
    proffessional_email = db.Column(db.String(100))
    proffessional_description = db.Column(db.String(100))
    proffessional_Service_type = db.Column(db.String(100))
    proffessional_years_of_experience = db.Column(db.Numeric(100))
    proffessional_photo = db.Column(db.String(100), default='static/default2.jpg')
    proffessional_location = db.Column(db.String(100))
    proffessional_pincode = db.Column(db.String(100))
    proffessional_rating = db.Column(db.DECIMAL(10, 2), default=0.00)
    proffessional_available = db.Column(db.Boolean, default=True)
    proffessional_flaged = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref=db.backref('proffessional', lazy=True))

class Client(db.Model):
    __tablename__ = 'client'
    client_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    client_bio = db.Column(db.String(100))
    client_email = db.Column(db.String(100))
    client_location = db.Column(db.String(100))
    client_total_spend = db.Column(db.Numeric(100))
    client_photo = db.Column(db.String(100), default='static/default1.jpg')
    client_pincode = db.Column(db.String(100))
    client_date_created = db.Column(db.DateTime, default=dt.now())
    client_flaged = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref=db.backref('client', lazy=True))

class Service(db.Model):
    __tablename__ = 'service'
    service_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_proffessional_id = db.Column(db.Integer, db.ForeignKey('proffessional.proffessional_id') , nullable=False)
    service_name = db.Column(db.String(100) , nullable=False)
    service_description = db.Column(db.String(100) , nullable=False)
    service_price = db.Column(db.Numeric(100) , nullable=False)
    service_photo = db.Column(db.String(100), default='static/default4.jpg' )
    service_flaged = db.Column(db.Boolean, default=False)
    service_date_created = db.Column(db.DateTime, default=dt.now(), nullable=False)
    
    proffessional = db.relationship('Proffessional', backref=db.backref('services', lazy=True))


class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_service_id = db.Column(db.Integer, db.ForeignKey('service.service_id') , nullable=False)
    order_client_id = db.Column(db.Integer, db.ForeignKey('client.client_user_id') , nullable=False)
    order_proffessional_id = db.Column(db.Integer, db.ForeignKey('proffessional.proffessional_user_id') , nullable=False)
    order_name = db.Column(db.String(100) , nullable=False)
    order_status = db.Column(db.String(100),default='Not Accepted' , nullable=False)
    order_date_created = db.Column(db.DateTime, default=dt.now() , nullable=False)
    order_date_accepted = db.Column(db.DateTime)
    order_date_completed = db.Column(db.DateTime)
    order_payment_amount = db.Column(db.Numeric(100) , nullable=False)
    order_flaged = db.Column(db.Boolean, default=False)

    service = db.relationship('Service', backref=db.backref('orders', lazy=True))

class Review(db.Model):
    __tablename__ = 'review'
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review_order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    review_rating = db.Column(db.Numeric(100) , nullable=False)
    review_comment = db.Column(db.String(100) , nullable=False)
    review_date_created = db.Column(db.DateTime, default=dt.now() , nullable=False)
    review_flaged = db.Column(db.Boolean, default=False)

    order = db.relationship('Order', backref=db.backref('reviews', lazy=True))


    
