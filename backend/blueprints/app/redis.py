import redis
import time
from flask_login import current_user

rs=redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

def establish_token():

    token = current_user.id + time.strftime("%H%M%S", time.localtime())
    tokendata = {'userid':current_user.id}

    rs.set(str(token), tokendata)
    rs.expire(str(token),60) 
    
    return str(token)