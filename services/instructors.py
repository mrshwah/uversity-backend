from models.users import User
from models.users import Instructor


#   Create Review
def create_instructor(instructor_args):
    user = User.objects(eb_id=instructor_args['user'])[0]
    instructor = Instructor(user=user)
    instructor.save()
    return instructor.to_dict()