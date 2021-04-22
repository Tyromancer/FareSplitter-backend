from app import db
from flask_login import UserMixin, current_user
import time


class Bill(db.Model):

    
    __tablename__ = 'bill'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Text)
    expendituremoney = db.Column(db.Integer) 
    income = db.Column(db.Integer) 
    money = db.Column(db.Integer) 
    date = db.Column(db.String(100))
    data = db.Column(db.String(100))

    def __init__(self, userid=None, expendituremoney=None, income=None, money=None, date=None, data=None):
        self.userid = current_user.id
        self.expendituremoney = expendituremoney
        self.income = income
        self.money = money
        self.date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.data = data
        self.update() 


    def update(self):
        db.session.add(self)
        db.session.commit()

#db.create_all()