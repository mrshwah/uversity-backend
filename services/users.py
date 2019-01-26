from models.users import User


def get_user(user_id):
    user = User.objects(eb_id=user_id)[0]
    return user.to_dict()


def create_user(user_args):
    user = User(eb_id=user_args['id'], oauth_token=user_args['oauth_token'])
    user.save()
    return user.to_dict()
