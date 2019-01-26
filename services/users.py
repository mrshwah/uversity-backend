from models.users import User


def get_user(user_id):
    user = User.objects(eb_id=user_id)[0]
    return user.to_dict()


def create_user(user_args):
    primary_email = ''
    for email in user_args['emails']:
        if email['primary']:
            primary_email = email['email']

    user = User(
        eb_id=user_args['id'],
        first_name=user_args['first_name'],
        last_name=user_args['last_name'],
        email=primary_email,
        oauth_token=user_args['oauth_token']
    )
    user = User(eb_id=user_args['id'])
    user.save()

    return user.to_dict()
