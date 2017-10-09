import os


class BaseConfig(object):
    SECRET_KEY = 'secret'
    DEBUG = True
    REDIS_URL = os.environ['REDIS_URL']


class TestingConfig(object):
    """Development configuration."""
    TESTING = True
    DEBUG = True
