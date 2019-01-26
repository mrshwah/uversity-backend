from flask_jwt_extended import JWTManager


def init_app(app):
    jwt = JWTManager(app)
