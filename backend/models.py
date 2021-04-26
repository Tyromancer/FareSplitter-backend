from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from backend.extensions import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(15), unique=True)

    payments = db.relationship('Payment', backref='user')

    def __init__(self, username):
        self.username = username

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }


class Payment(db.Model):
    __tablename__ = 'Payment'
    id = db.Column(db.Integer, primary_key=True)

    # Many to One relationship:
    # Multiple payments exist, but each payment only refers to one User
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    # Many to One relationship:
    # Multiple payments exist, but each payment only belongs to one Transaction
    transaction_id = db.Column(db.Integer, db.ForeignKey('Payment.id'), nullable=False)

    # transaction = db.relationship('Transaction', backref='payment')
    amount = db.Column(db.Float)

    def __init__(self, user_id, transaction_id, amount=0.0):
        self.user_id = user_id
        self.transaction_id = transaction_id
        self.amount = amount

    def to_dict(self):
        user = User.query.filter_by(id=self.user_id).first()
        return {
            'id': self.id,
            'username': user.username,
            'amount': self.amount
        }


class Transaction(db.Model):
    __tablename__ = 'Transaction'
    id = db.Column(db.Integer, primary_key=True)

    # One to many relationship:
    # For any single transaction, it can have many payments
    payments = db.relationship('Payment', backref='transaction')

    time = db.Column(db.DateTime())

    def __init__(self):
        self.time = datetime.now()

    def to_dict(self):

        payments = list()
        for payment in Payment.query.filter_by(transaction_id=self.id).all():
            payments.append(payment.to_dict())

        res = {
            'payments': payments,
            'time': self.time
        }

        return jsonify(res), 200
