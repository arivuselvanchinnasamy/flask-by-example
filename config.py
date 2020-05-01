import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object) :
    DEBUG= False
    TESTING= False
    CRSF_Enabled= True
    SECRET_KEY="mysecret"

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True