from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from models import database_proxy
from api import ReportPage, DriverPage
from peewee import *


def create_app(config=None):

    app = Flask('Report of Monaco racing 2k18')
    app.config.from_object(config)
    swagger = Swagger(app)
    api = Api(app)
    db = SqliteDatabase(app.config['DATABASE'])
    database_proxy.initialize(db)

    api.add_resource(ReportPage, '/api/v1/report/')
    api.add_resource(DriverPage, '/api/v1/report/<driver_id>')

    return app



