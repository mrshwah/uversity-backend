from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.aggregates import get_aggregate


class Aggregates(Resource):

    @jwt_required
    def get(self, instructor_id):
        aggregate = get_aggregate(instructor_id)
        return {'aggregate': aggregate}
