import flask
import json
from flask import Flask, jsonify, Blueprint, current_app

from backend.extensions import db
from backend.models import User
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
