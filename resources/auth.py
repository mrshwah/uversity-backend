from flask_restful import Resource, reqparse
import services.eventbrite as eb
import services.users as users

post_parser = reqparse.RequestParser()
post_parser.add_argument('access_code')


class Auth(Resource):
    def post(self):
        args = post_parser.parse_args()
        oauth_token = args['access_code']
        user_args = eb.get_user(oauth_token)
        user = users.create_user(user_args)
        return {'user': user}
