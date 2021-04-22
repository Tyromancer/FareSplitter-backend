__author__ = 'Xiongc2'
from app import Flask, cache
from ..index import index
from flask import render_template, request, session, redirect
from flask_login import current_user
from app.DB_module import Bill
import json

@index.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('game.html')
    else:
        return render_template('index.html')


@index.route('/roc', methods=["GET","POST"])
def roc():
    if current_user.is_authenticated:
        if request.method == 'POST':
            jsondata = request.json
            page = jsondata['page']
            page_size = 25
            data = Bill.query.filter_by(userid=current_user.id).limit(page_size).offset((page - 1)*page_size)

            data = [{
                'date':i.date,
                'data':i.data,
                'expendituremoney':i.expendituremoney,
                'income':i.income,
                'money':i.money
            }for i in data]

            return json.dumps(data)

        else:
            return render_template('roc.html')