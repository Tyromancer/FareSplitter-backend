from app import db
from flask_login import UserMixin, current_user

class User(db.Model, UserMixin):

    
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    Users = db.Column(db.Text)
    money = db.Column(db.Integer)

    
    def __init__(self, Users=None, money=0):
        self.Users = Users
        self.money = money
        self.update() 

    
    def update(self):
        db.session.add(self)
        db.session.commit()