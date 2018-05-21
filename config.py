import os

class Config:
    '''
    Describes the general configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://richi:'+DATABASE_PASS+'@localhost/pitchit'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #Simple MDE configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://richi:'+DATABASE_PASS+'@localhost/pitchit'

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://richi:'+DATABASE_PASS+'@localhost/pitchit'
    DEBUG = True

class TestConfig(Config):
    '''
    Test configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://richi:'+DATABASE_PASS+'@localhost/pitchit_test'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}