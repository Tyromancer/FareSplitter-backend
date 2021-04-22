__author__ = 'Xiongc2'
from app import Flask, cache, login_manager
from ..User import User
from flask import render_template, request, session, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app.DB_User import User
import json

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@User.route('/auth', methods=["POST"])
def authUser():
    if current_user.is_authenticated:
        return json.dumps({'code': 0, 'text': 'You have logged in'})

    else:
        if request.method == 'POST':

            
            jsondata = request.json
            print(request.json)

            
            if jsondata['User'] == '':
                return json.dumps({'code': 0, 'text': 'Your username cannot be null'})
            else:
                user = User.query.filter_by(Users = jsondata['User']).first()
                if(user):
                    session.permanent = True
                    login_user(user, remember=True)
                    return json.dumps({'code': 1, 'text': 'Sucessful'})
                else:
                    return json.dumps({'code': 0, 'text': 'No username'})


@User.route('/register', methods=["POST"])
def registerUser():
    if current_user.is_authenticated:
        return json.dumps({'code': 0, 'text': 'You have logged in'})

    else:
        if request.method == 'POST':
            print(request.json)

            
            jsondata = request.json

            
            if jsondata['User'] == '':
                return json.dumps({'code': 0, 'text': 'Your username cannot be null'})
            else:
                User(Users = jsondata['User'])
                
                return json.dumps({'code': 1, 'text': 'Sucessful'})

@User.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.home'))