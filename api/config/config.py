import os
from datetime import timedelta
from dotenv import load_dotenv

# load_env
load_dotenv(override=True)


class Config:
    FLASK_ENV = os.getenv('FLASK_ENV')
    PORT = os.getenv('PORT')
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH', 'superhero')
    

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO')
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI')
    CORS_ORIGINS = ["*"]


class TestConfig(Config):
    FLASK_ENV = 'test'
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI')
    NEXACT_ADMIN = 'test-admin@nexact.ci'
    CORS_ORIGINS = ['*']


class StageConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('STAGE_DATABASE_URI')
    CORS_ORIGINS = []


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI')
    CORS_ORIGINS = []


config_dict = {
    'dev': DevConfig,
    'test': TestConfig,
    'stage': StageConfig,
    'prod': ProdConfig,

    'default': DevConfig,
}
