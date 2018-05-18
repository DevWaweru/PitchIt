import os

class Config:
    '''
    Describes the general configurations
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://richi:pass@localhost/pitchit'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProdConfig(Config):

class DevConfig(Config):

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}