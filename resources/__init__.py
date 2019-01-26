from flask_restful import Api
from .auth import Auth
from .eventbrite import ClientId
from .users import Users


def init_app(app):
    api = Api(app)
    api.add_resource(Auth, '/auth')
    api.add_resource(ClientId, '/client_id')
    api.add_resource(Users, '/users/<string:user_id>')
