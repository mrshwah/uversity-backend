from datetime import datetime
from models.courses import Course


# Services for Course
def get_course(course_id):
    course = Course.objects(eb_id=course_id)[0]
    return course.to_dict()


def get_courses():
    courses = [course.to_dict() for course in Course.objects()]
    return courses


def create_course(course_args):
    course = Course(eb_id=course_args['eb_id'],
                    name=course_args['name'],
                    start=datetime.strptime(course_args['start'], "%Y-%m-%dT%H:%M:%SZ"),
                    end=datetime.strptime(course_args['end'], "%Y-%m-%dT%H:%M:%SZ"),
                    capacity=course_args['capacity'])
    course.save()
    return course.to_dict()


# Services for CourseList
def get_courses(course_args):
    courses = [ob.to_dict() for ob in Course.objects()]
    return courses
