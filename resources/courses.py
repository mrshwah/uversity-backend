from flask_restful import Resource, reqparse
from models.courses import Course as CourseModel
import services.eventbrite as eb
import services.courses as event


parser = reqparse.RequestParser()
parser_args = [
    'id', 'teacher', 'title', 'location', 'category',
    'difficulty', 'image_links', 'start_data_and_time', 'end_date_and_time',
    'student_list', 'capacity'
]
for arg in parser_args:
    parser.add_argument(arg)


# Methods for a single course
class Course(Resource):
    def get(self):
        pass

    def post(self):
        args = parser.parse_args()
        # course_args = eb.post_event(parser_args)
        course = event.create_course(parser_args)
        return {'course': course}

    def put(self):
        pass

    def delete(self):
        pass


# Methods for a list of courses
class CourseList(Resource):
    def get(self):
        pass
