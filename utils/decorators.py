from flask_jwt_extended import get_jwt_identity


def check_jwt_identity(func):
    def wrapper(*args, **kwargs):
        if get_jwt_identity() != kwargs['user_id']:
            return {'error': True, 'message': 'You do not have permission to perform that function.'}, 403
        return func(*args, **kwargs)
    return wrapper
