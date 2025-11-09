import os
import uuid
from flask import Flask
from flask_restx import Api
# from .config.config import config_dict


def create_app(config_name='default'):

    # flask app
    app = Flask(__name__)
    # app.config.from_object(config_dict[config_name])

    api = Api(
        app,
        title="Nexact web service",
        version='1.1',
        # security='accessToken',
        # authorizations={
        #     'accessToken': access_token_security,
        #     'refreshToken': refresh_token_security
        # }
    )

    return app