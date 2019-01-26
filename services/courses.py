from models.courses import Course


# Services for Course
def create_course(course_args):
    print(course_args)
    # course = Course(eb_id=course_args['id'],
    #                 teacher=course_args['teacher'],
    #                 title=course_args['name']['text'],
    #                 location=,
    #                 category=,
    #                 difficulty=,
    #                 image_links=,
    #                 start_date_and_time=,
    #                 end_date_and_time=,
    #                 student_list=,
    #                 capacity=)



# Services for CourseList
def get_courses(course_args):
    courses = [ob.to_dict() for ob in Course.objects()]
    return courses
