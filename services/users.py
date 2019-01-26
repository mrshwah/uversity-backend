from models.users import User


def create_user(user_args):
    user = User(eb_id=user_args['id'])
    user.save()
    return user.to_dict()
