from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.users import User as UserModel
from services.users import update_user, delete_user, get_user

put_parser = reqparse.RequestParser()
put_parser.add_argument('interests', action='append')
# put_parser.add_argument('student_reputation')


class Users(Resource):
    @jwt_required
    def get(self, user_id):
        try:
            user = get_user(user_id)
        except IndexError:
            return {'error': True, 'message': 'User not found!'}

        return user

    @jwt_required
    def put(self, user_id):
        args = put_parser.parse_args()
        try:
            updated_user = update_user(args, user_id)
        except IndexError:
            return {'error': True, 'message': 'User not found!'}

        return {'user': updated_user}

    @jwt_required
    def delete(self, user_id):
        try:
            resp = delete_user(user_id)
        except IndexError:
            return {'error': True, 'message': 'User not found!'}

        return resp
