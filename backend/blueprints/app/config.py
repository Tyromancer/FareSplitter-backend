from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/slotmachine?charset=utf8'

SQLALCHEMY_TRACK_MODIFICATIONS = True

BCRYPT_LOG_ROUNDS = 1