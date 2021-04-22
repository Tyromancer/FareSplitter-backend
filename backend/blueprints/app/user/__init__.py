__author__ = 'Xiongc2'

from flask import Blueprint
account = Blueprint('user', __name__)
from ..account import views