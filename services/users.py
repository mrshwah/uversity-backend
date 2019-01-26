from models.users import User


def create_user(user_args):
    primary_email = ''
    for email in user_args['emails']:
        if email['primary']:
            primary_email = email['email']

    user = User(
        eb_id=user_args['id'],
        first_name=user_args['first_name'],
        last_name=user_args['last_name'],
        email=primary_email
    )
    user.save()

    return user.to_dict()
