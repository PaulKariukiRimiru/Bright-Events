# config.py

import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = 'secret'
    JWT_SECRET_KEY = 'jwt secret key for encryption purposes'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 465

    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    MAIL_USERNAME = 'mikethedeveloper7@gmail.com'
    MAIL_PASSWORD = 'Ripper10131994!'
    ADMINS = ['mikethedeveloper7@gmail.com']
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
class TesingConfig(Config):
    """Configuration for test"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql+psycopg2://mike:10131994@localhost/test_db')
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TesingConfig,
    'configobj':Config,
    'SECRET_KEY':'secret_key',
    'limit':2
}
