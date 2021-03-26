import flask
import json
from flask import Flask, jsonify, Blueprint, current_app


# create blueprint for api endpoints
api_bp = Blueprint('api', __name__)


@api_bp.route('/api/hello-world')
def hello_world():
    resp = {
        'msg': 'Hello World!'
    }

    return jsonify(resp)
