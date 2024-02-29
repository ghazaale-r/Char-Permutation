import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secure_secret_key'
    DEBUG = os.environ.get('DEBUG') or False
