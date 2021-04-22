import flask
import json
from flask import Flask, jsonify, Blueprint, current_app
from flask_sqlalchemy import SQLAlchemy
from app.index import index
from app.user import user
from app.bill import bill


import settings.BaseConfig as BaseConfig 

# create blueprint for api endpoints
api_bp = Blueprint('api', __name__)
api_bp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/flask_ex'
api_bp.config.from_object(BaseConfig)
db = SQLAlchemy(api_bp)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) 


@api_bp.route('/api/hello-world')
def hello_world():
    resp = {
        'msg': 'Hello World!'
    }

    return jsonify(resp)

@app_bp.route('/add_user_test',methods=['GET','POST'])
def get_bill():
    user1 = User(name='wang',email='wang@163.com',pswd='123456',role_id=role1.id)
    user2 = User(name='zhang',email='zhang@189.com',pswd='201512',role_id=role2.id)
    user3 = User(name='chen',email='chen@126.com',pswd='987654',role_id=role2.id)
    user4 = User(name='zhou',email='zhou@163.com',pswd='456789',role_id=role1.id)
    db.session.add_all([user1,user2,user3,user4])
    db.session.commit()



api_bp.register_blueprint(index, url_prefix='/index')
api_bp.register_blueprint(user, url_prefix='/user')
api_bp.register_blueprint(bill, url_prefix='/bill')
