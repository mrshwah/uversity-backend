from models.instructors import Instructor


def delete_instructor(instructor_args):
    instructor = Instructor.objects(id__exists=instructor_args['id'])
    instructor.delete()
    return True
