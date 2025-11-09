import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_admin import Admin
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap

# from flask_login import LoginManager
# from flask_jwt_extended import JWTManager


class Base(DeclarativeBase):
    pass


# load_env
load_dotenv(override=True)
RATELIMIT_HOUR = os.getenv('RATELIMIT_HOUR')
RATELIMIT_DAY = os.getenv('RATELIMIT_DAY')

# extensions
db = SQLAlchemy(model_class=Base)
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
admin_ext = Admin(name='Masjid Admin')
limiter = Limiter(
    key_func=get_remote_address, default_limits=[RATELIMIT_HOUR, RATELIMIT_DAY], storage_uri="memory://"
)
bootstrap = Bootstrap()

# jwt = JWTManager()
# login_manager = LoginManager()
# login_manager.login_view = 'login'