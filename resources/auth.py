from flask_restful import Resource, reqparse
import services.eventbrite as eb
from models.users import User

post_parser = reqparse.RequestParser()
post_parser.add_argument('access_code')


class Auth(Resource):
    def post(self):
        args = post_parser.parse_args()
        oauth_token = eb.get_oauth_token(args['access_code'])
        user = eb.get_user(oauth_token)
        user_in_db = User(eb_id=user['id']).save()
        print(user_in_db)
        return {'user': user}
