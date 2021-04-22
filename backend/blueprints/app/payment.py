__author__ = 'Xiongc 2'
from app import db
from app.DB_account import Account
from app.DB_module import Bill
from flask_login import current_user

def purchase():
    money = int(Account.query.filter_by(id = current_user.id).first().money) - 5
    db.session.query(Account).filter(Account.id == current_user.id).update({Account.money:int(money)})
    db.session.commit()

def gamereward(rewardtype):
    if int(rewardtype) == 2:
        money = int(Account.query.filter_by(id = current_user.id).first().money) + 20
        
    elif int(rewardtype) == 3:
        money = int(Account.query.filter_by(id = current_user.id).first().money) + 50

    else:
        money = Account.query.filter_by(id = current_user.id).first().money

    db.session.query(Account).filter(Account.id == current_user.id).update({Account.money:int(money)})
    db.session.commit()