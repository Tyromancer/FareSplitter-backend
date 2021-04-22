__author__ = 'Xiongc2'

from flask import Blueprint
index = Blueprint('bill', __name__)
from ..index import views