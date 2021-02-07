import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///api.db' + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


