from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
import services.eventbrite as eb
import services.users as users

post_parser = reqparse.RequestParser()
post_parser.add_argument('access_code')


class Auth(Resource):
    def post(self):
        args = post_parser.parse_args()
        oauth_token = args['access_code']
        user_args = eb.get_user(oauth_token)
        try:
            user = users.get_user(user_args['id'])
        except IndexError:
            user_args['oauth_token'] = oauth_token
            user = users.create_user(user_args)
        access_token = create_access_token(identity=user['eb_id'])
        return {'user': user, 'access_token': access_token}
