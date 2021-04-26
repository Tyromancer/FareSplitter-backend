import flask
import json
from flask import Flask, jsonify, Blueprint, current_app

from backend.extensions import db
from backend.models import User, Payment, Transaction
# create blueprint for api endpoints
api_bp = Blueprint('api', __name__)


@api_bp.route('/api/hello-world')
def hello_world():
    resp = {
        'msg': 'Hello World!'
    }

    return jsonify(resp)


@api_bp.route('/api/add-user', methods=['POST'])
def add_user():
    req = flask.request.get_json()

    username = req['username'].strip()

    if User.query.filter_by(username=username).first():
        res = {
            'msg': 'Username already registered'
        }

        return jsonify(res), 400

    user = User(username)
    db.session.add(user)
    db.session.commit()

    res = {
        'msg': 'ok'
    }

    return jsonify(res), 200


@api_bp.route('/api/get-all-users', methods=['GET'])
def get_all_users():
    users = list()
    for user in User.query.all():
        users.append(user.to_dict())

    res = {
        'msg': 'ok',
        'users': users
    }

    return jsonify(res), 200


# use for test only
# payments should be created with transaction in a batch, not individually
@api_bp.route('/api/add-payment', methods=['POST'])
def add_payment():
    req = flask.request.get_json()
    print(req)

    username = req['username']
    amount = req['amount']

    user = User.query.filter_by(username=username).first()
    if user is None:
        res = {
            'msg': f'User with name {username} does not exist'
        }

        return jsonify(res), 400
    
    payment = Payment(user.id, 0, amount=amount)

    db.session.add(payment)
    db.session.commit()

    res = {
        'msg': 'ok'
    }

    return jsonify(res), 200
    pass

@api_bp.route('/api/get-all-payments', methods=['GET'])
def get_all_payments():
    # req = flask.request.get_json()

    payments = list()
    for payment in Payment.query.all():
        payments.append(payment.to_dict())
    
    res = {
        'payments': payments
    }

    return jsonify(payments), 200


@api_bp.route('/api/add-transaction', methods=['POST'])
def add_transaction():

    req = flask.request.get_json()

    transaction = Transaction()
    db.session.add(transaction)

    for payment in req['payments']:
        username = payment['username']
        amount = payment['amount']


        user = User.query.filter_by(username=username).first()

        if user is None:
            res = {
                'msg': f'User with name {username} does not exist'
            }

            return jsonify(res), 400
        
        payment = Payment(user_id=user.id, transaction_id=transaction_id, amount=amount)
        db.session.add(payment)
    
    db.session.commit()

    res = {
        'msg': 'ok'
    }

    return jsonify(res), 200

@api_bp.route('/api/get-all-transactions', method=['GET', 'POST'])
def get_all_transactions():
    transactions = list()

    for transaction in Transaction.query.all():
        transactions.append(transaction.to_dict())
    
    res = {
        'msg': 'ok',
        'transactions': transactions
    }


    return jsonify(res), 200