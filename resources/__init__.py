from flask_restful import Api
from .auth import Auth


def init_app(app):
    api = Api(app)
    api.add_resource(Auth, '/auth')
