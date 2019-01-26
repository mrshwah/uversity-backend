from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.users import User as UserModel


class Users(Resource):
    @jwt_required
    def get(self):
        users = [ob.to_dict() for ob in UserModel.objects()]
        return users

    def put(self):
        pass

    def delete(self):
        pass
