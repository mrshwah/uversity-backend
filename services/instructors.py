from models.users import User, Instructor


#   Create Review
def create_instructor(user_id):
    instructor = Instructor()
    instructor.save()
    user = User.objects.get(eb_id=user_id)
    user.instructor = instructor
    user.save()
    return user.to_dict()


def get_instructor(instructor_id):
    instructor = User.objects.get(instructor=instructor_id)
    return instructor.to_dict()
