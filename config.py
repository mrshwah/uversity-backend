import os


class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGODB_HOST = os.environ.get("MONGODB_HOST")
    MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")
    MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")
    MONGODB_PORT = int(os.environ.get("MONGODB_PORT"))
    MONGODB_DB = os.environ.get("MONGODB_DB")
    EB_CLIENT_ID = os.environ.get("EB_CLIENT_ID")
    EB_CLIENT_SECRET = os.environ.get("EB_CLIENT_SECRET")
    JWT_ACCESS_TOKEN_EXPIRES = False


class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
