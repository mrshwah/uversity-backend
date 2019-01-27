from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.instructors import create_instructor, get_instructor


class Instructor(Resource):
    @jwt_required
    def get(self, id):
        instructor = get_instructor(id)
        return {'instructor': instructor}

    def put(self):
        #   This method should be used in the case of updating reviews.
        pass

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        try:
            instructor = create_instructor(user_id)
        except Exception:
            return {'error': True, 'message': 'Instructor already exists for this user.'}
        return {'instructor': instructor}
