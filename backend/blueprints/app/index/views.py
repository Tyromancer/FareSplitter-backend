__author__ = 'Xiongc2'
from app import Flask, cache
# from ..Bill_conlcude import Bill_conlcude
from flask import render_template, request, session, redirect
from flask_login import current_user
from app.redis import establish_token
from app.DB_account import Account
from app.DB_module import Bill
from app.payment import purchase, Bill_conlcudereward
import random

import json

@Bill_conlcude.route('/get-result', methods=["POST"])
def result():
    if current_user.is_authenticated:
        if request.method == 'POST':
            #jsondata = request.json

            #token = jsondata['token']

            user = Account.query.filter_by(id=current_user.id).first()

            if user.money > 0:

                purchase()
               

                a = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
                b = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
                c = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])

                reward, rewardtype, roc = result_reward(a, b, c)
                
                jsons = {
                    'code':1,
                    'a':a,
                    'b':b,
                    'c':c,
                    'reward':reward,
                    'type':rewardtype,
                    'money':Account.query.filter_by(id=current_user.id).first().money,
                    'roc_date':roc.date,
                    'roc_expendituremoney':roc.expendituremoney,
                    'roc_income':roc.income,
                    'roc_money':roc.money,
                    'data':roc.data
                }

                print(jsons)

                return json.dumps(jsons)

            else:
                return json.dumps({'code':0, 'text':'No enough money'})

        else:
            pass
    else:
        pass

def result_reward(a, b, c):
    data = str(a) + " - " + str(b) + " - " + str(c)
    if a == b & a == c:
        Bill_conlcudereward(3)
        roc = Bill(expendituremoney=5, income=50, money=Account.query.filter_by(id=current_user.id).first().money, data=data)
        return 50, 3, roc

    elif a == b or b == c:
        Bill_conlcudereward(2)
        roc = Bill(expendituremoney=5, income=20, money=Account.query.filter_by(id=current_user.id).first().money, data=data)
        return 20, 2, roc

    elif a == c:
        Bill_conlcudereward(2)
        roc = Bill(expendituremoney=5, income=20, money=Account.query.filter_by(id=current_user.id).first().money, data=data)
        return 20, 31, roc

    else:
        roc = Bill(expendituremoney=5, income=0, money=Account.query.filter_by(id=current_user.id).first().money, data=data)
        return 0, 0, roc

@Bill_conlcude.route('/get-tokon')
def gettokon():
    if current_user.is_authenticated:
        
        token = establish_token()

        return json.dumps({'token':token, 'outtime':60})