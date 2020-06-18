import os

from flask import Flask
from flask_restful import Api

from .database import db
from .api import ListCreateCustomer, GetUpdateDeleteCustomer

from . import config


def app_factory():
    app = Flask(__name__)

    app.config.from_object(config.ProductionConfig)
    if os.environ.get("FLASK_ENV") == "development":
        app.config.from_object(config.DevelopmentConfig)

    app.config["SECRET_KEY"] = "jeeuewifiueeowuegeeiueyoeiuefogfyfefe"
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb+srv://austino:austino19928@cluster0-qht2p.mongodb.net/custdb?retryWrites=true&w=majority',
        'connect': False
    }

    # register extension
    api = Api(app)
    db.initialize_app(app)

    # register endpoint
    api.add_resource(ListCreateCustomer, "/v1/customer")
    api.add_resource(GetUpdateDeleteCustomer, "/v1/customer/<string:cust_id>")

    return app


myapp = app_factory()
