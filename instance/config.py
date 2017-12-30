# config.py

import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = 'secret'
    JWT_SECRET_KEY = 'jwt secret key for encryption purposes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql+psycopg2://mike:10131994@localhost/bright_events')
class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql+psycopg2://mike:10131994@localhost/bright_events')

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'configobj':Config,
    'SECRET_KEY':'secret_key'
}
