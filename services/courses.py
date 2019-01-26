from datetime import datetime
from models.courses import Course


# Services for Course
def get_course(course_id):
    course = Course.objects(eb_id=course_id)[0]
    return course.to_dict()


def create_course(course_args):
    course = Course(eb_id=course_args['eb_id'],
                    name=course_args['name'],
                    start=datetime.strptime(course_args['start'], "%Y-%m-%dT%H:%M:%SZ"),
                    end=datetime.strptime(course_args['end'], "%Y-%m-%dT%H:%M:%SZ"),
                    capacity=course_args['capacity'])
    course.save()
    return course.to_dict()


def update_course(course_id, course_args):
    course = Course.objects(eb_id=course_id)[0]
    course.name = course_args['name']
    course.start = datetime.strptime(course_args['start'], "%Y-%m-%dT%H:%M:%SZ")
    course.end = datetime.strptime(course_args['end'], "%Y-%m-%dT%H:%M:%SZ")
    course.capacity = course_args['capacity']
    course.save()
    # need to update event in eventbrite (create EB service to put event to EB)
    return course.to_dict()


# Services for CourseList
def get_courses(course_args):
    courses = [ob.to_dict() for ob in Course.objects()]
    return courses
