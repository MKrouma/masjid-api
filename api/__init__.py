import os
import uuid
from flask import Flask
from flask_restx import Api
from .config.config import config_dict
from .cores.extensions import db, migrate, ma, cors, limiter, bootstrap, admin_ext
from .admin.view import (
    PrayersView, MasjidsView
)
from .models.prayers import Prayer
from .models.masjids import Masjid
from api.commands import restart_db, add_prayers, add_masjids
from api.ressources.prayers.routes import prayer_ns


def create_app(config_name='default'):

    # flask app
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    # flask extensions
    register_extensions(app)

    api = Api(
        app,
        title="Masjid web service",
        version='1.1',
        # security='accessToken',
        # authorizations={
        #     'accessToken': access_token_security,
        #     'refreshToken': refresh_token_security
        # }
    )

    # registers
    register_blueprints(api, app)
    register_shellcontext(app)
    register_admin_interfaces(config_name)
    register_commands(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    limiter.init_app(app)
    admin_ext.init_app(app)
    cors.init_app(
        app,
        resources={
            r"/v1/*": {
                "origins": app.config.get('CORS_ORIGINS'),
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
                "allow_headers": [
                    "Content-Type",
                    "Authorization",
                    "Access-Control-Allow-Credentials"
                ],
                "supports_credentials": True,
                "max_age": 3600
            }
        }
    )
    bootstrap.init_app(app)

    # # to add
    # jwt.init_app(app)
    # login_manager.init_app(app)
    # bcrypt.init_app(app)
    # cache.init_app(app)
    # csrf_protect.init_app(app)
    # debug_toolbar.init_app(app)
    # flask_static_digest.init_app(app)

    return None


def register_blueprints(api, app):
    """Register Flask blueprints."""
    api.add_namespace(prayer_ns, path='/v1/prayers')

    return None


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {
            "db": db
        }

    app.shell_context_processor(shell_context)


def register_admin_interfaces(config_name):
    # admin interface
    if config_name != 'test':
        admin_ext.add_view(PrayersView(Prayer, db.session))
        admin_ext.add_view(MasjidsView(Masjid, db.session))
    return None


def register_commands(app):
    """Register commands functions."""

    # app.cli.add_command(restart_db)
    app.cli.add_command(add_prayers)
    app.cli.add_command(add_masjids)