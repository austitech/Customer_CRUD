
from flask import Flask
from flask_restful import Api

from .database import db
from .api import ListCreateCustomer, GetUpdateDeleteCustomer

from . import config


def app_factory(testing=False):
    app = Flask(__name__)

    app.config.from_object(config.ProductionConfig)
    if testing:
        app.config.from_object(config.DevelopmentConfig)

    # register extension
    api = Api(app)
    db.initialize_app(app)

    # register endpoint
    api.add_resource(ListCreateCustomer, "/v1/customer")
    api.add_resource(GetUpdateDeleteCustomer, "/v1/customer/<string:cust_id>")

    return app
