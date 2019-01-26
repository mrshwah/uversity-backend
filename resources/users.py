from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from utils.decorators import check_jwt_identity
from services.users import update_user, delete_user, get_user

put_parser = reqparse.RequestParser()
put_parser.add_argument('interests', action='append')
put_parser.add_argument('course_history', action='append')
# put_parser.add_argument('student_reputation')


class User(Resource):
    @jwt_required
    def get(self, user_id):
        try:
            user = get_user(user_id)
        except IndexError:
            return {'error': True, 'message': 'User not found!'}, 404

        return user

    @jwt_required
    @check_jwt_identity
    def put(self, user_id):
        args = put_parser.parse_args()
        try:
            updated_user = update_user(args, user_id)
        except IndexError:
            return {'error': True, 'message': 'User not found!'}, 404

        return {'user': updated_user}

    @jwt_required
    @check_jwt_identity
    def delete(self, user_id):
        try:
            resp = delete_user(user_id)
        except IndexError:
            return {'error': True, 'message': 'User not found!'}, 404

        return resp
