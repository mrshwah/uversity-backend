from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
import services.eventbrite as eb
import services.courses as courses
import services.users as users

course_parser = reqparse.RequestParser()
course_parser.add_argument('name')
course_parser.add_argument('description')
course_parser.add_argument('start', type=dict)
course_parser.add_argument('end', type=dict)
course_parser.add_argument('capacity', type=int)
course_parser.add_argument('category')

start_parser = reqparse.RequestParser()
start_parser.add_argument('timezone', location='start')
start_parser.add_argument('utc', location='start')

end_parser = reqparse.RequestParser()
end_parser.add_argument('timezone', location='end')
end_parser.add_argument('utc', location='end')


class Course(Resource):
    @jwt_required
    def get(self, course_id):
        try:
            course = courses.get_course(course_id)
        except IndexError:
            return {'error': True, 'message': 'Course not found!'}, 404
        return {'course': course}

    @jwt_required
    def post(self):
        args = course_parser.parse_args()
        start_args = start_parser.parse_args(args)
        end_args = end_parser.parse_args(args)
        user_id = get_jwt_identity()
        oauth_token = users.get_user(user_id)['oauth_token']
        event_args = {'event': {'name': {'html': '<p>{}<p>'.format(args['name'])},
                                'description': args['description'],
                                'start': {'timezone': start_args['timezone'], 'utc': start_args['utc']},
                                'end': {'timezone': end_args['timezone'], 'utc': end_args['utc']},
                                'currency': 'USD', 'capacity': args['capacity']}}
        event_id = eb.create_event(oauth_token, event_args).id
        args['eb_id'] = event_id
        args['start'] = start_args['utc']
        args['end'] = end_args['utc']
        args['instructor'] = user_id
        course = courses.create_course(args)
        return {'course': course}

    @jwt_required
    def put(self, course_id):
        try:
            course = courses.get_course(course_id)
        except IndexError:
            return {'error': True, 'message': 'Course not found!'}, 404
        args = course_parser.parse_args()
        start_args = start_parser.parse_args(args)
        end_args = end_parser.parse_args(args)
        user_id = get_jwt_identity()
        oauth_token = users.get_user(user_id)['oauth_token']
        event_args = {'event': {'name': {'html': '<p>{}<p>'.format(args['name'])},
                                'description': args['description'],
                                'start': {'timezone': start_args['timezone'], 'utc': start_args['utc']},
                                'end': {'timezone': end_args['timezone'], 'utc': end_args['utc']},
                                'currency': 'USD', 'capacity': args['capacity']}}
        eb.update_event(oauth_token, course_id, event_args)
        args['start'] = start_args['utc']
        args['end'] = end_args['utc']
        course = courses.update_course(course_id, args)
        return {'course': course}

    @jwt_required
    def delete(self, course_id):
        try:
            course = courses.get_course(course_id)
        except IndexError:
            return {'error': True, 'message': 'Course not found!'}, 404
        user_id = get_jwt_identity()
        oauth_token = users.get_user(user_id)['oauth_token']
        eb.delete_event(oauth_token, course_id)
        deleted = courses.delete_course(course_id)
        return {'deleted': deleted}


# Methods for a list of courses
class CourseList(Resource):
    @jwt_required
    def get(self, category):
        course_list = courses.get_courses_by_category(category)
        return {'courses': course_list}


class CourseEnroll(Resource):
    @jwt_required
    def post(self, course_id):
        print(course_id)
        user_id = get_jwt_identity()
        course = courses.enroll_user_in_course(course_id, user_id)
        return {'course': course}