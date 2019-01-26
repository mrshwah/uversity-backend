from flask_restful import Resource
from models.users import User as UserModel


class Users(Resource):
    def get(self):
        users = [ob.to_dict() for ob in UserModel.objects()]
        return users

    def put(self):
        pass

    def delete(self):
        pass
