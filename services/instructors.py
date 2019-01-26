from models.users import User, Instructor


#   Create Review
def create_instructor(user_id):
    user = User.objects.get(eb_id=user_id)
    if user.instructor:
        raise Exception
    instructor = Instructor()
    instructor.save()
    user.instructor = instructor
    user.save()
    return {'user': user.to_dict()}


def get_instructor(instructor_id):
    instructor = User.objects.get(instructor=instructor_id)
    return {'user': instructor.to_dict()}
