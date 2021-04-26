# TODO: detect platform and change connection string prefix accordingly
prefix = 'sqlite:///'


class BaseConfig(object):
    DEBUG = True

    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = prefix + 'fare.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
