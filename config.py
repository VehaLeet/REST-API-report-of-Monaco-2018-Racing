
class Config:
    '''Base config'''
    APPLICATION_ROOT = r'\\'
    DATA_FOLDER = 'data'
    JSON_SORT_KEYS = False
    SWAGGER = {'title': 'Monaco racing 18, API', 'uiversion': 2}


class Test(Config):
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
    DATABASE = ':memory:'
    SERVER_NAME = 'localhost'


class Dev(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE = 'drivers.db'
