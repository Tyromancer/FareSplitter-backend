__author__ = 'Xiongc2'
#!bin/python3.6
from app import api, blueprint

if __name__ == '__main__':
    api.run(host='127.0.0.1', port=80, debug=True, threaded=True)