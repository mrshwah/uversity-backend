from flask_restful import Api
from .auth import Auth
from .eventbrite import ClientId
from .reviews import Review
from .reviews import ReviewList
from .users import User
from .courses import Course


def init_app(app):
    api = Api(app)
    api.add_resource(Auth, '/auth')
    api.add_resource(ClientId, '/client_id')
    api.add_resource(ReviewList, '/reviews')
    api.add_resource(Review, '/review/<string:id>')
    api.add_resource(User, '/user/<string:user_id>')
    api.add_resource(Course, '/course', '/course/<int:course_id>')

