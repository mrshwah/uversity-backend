from flask_restful import Resource, reqparse
from services.instructors import create_instructor
from models.users import Instructor as InstructorModel


post_parser = reqparse.RequestParser()
post_parser.add_argument('user')


class Instructor(Resource):
    def get(self, id):
        instructor = InstructorModel.objects(id__exists=id)[0]
        instructor = instructor.to_dict()
        return {'instructor': instructor}

    def put(self):
        #   This method should be used in the case of updating reviews.
        pass

    def post(self):
        args = post_parser.parse_args()
        instructor_args = args
        instructor = create_instructor(instructor_args)
        return {'instructor': instructor}

    # Doesn't work
    def delete(self, id):
        instructor = InstructorModel.objects.get(id)    #idfk dood
        user_child = instructor['user']
        if instructor.delete():
            user_child.delete()
            return {"message": "success!"}
        else:
            return {"message": "failed"}
