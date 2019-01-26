from flask_restful import Resource
from models.instructors import Instructor as InstructorModel


class Instructors(Resource):
    def get(self):
        instructors = [ob.to_dict() for ob in InstructorModel.objects()]
        return instructors

    def put(self):
        pass

    def delete(self):
        pass
