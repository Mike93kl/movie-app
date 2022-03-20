from functools import wraps
from flask import jsonify
from flask_login import current_user

def role_auth(roles):
    def validate_role(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if current_user.role not in roles:
                return jsonify({'message': 'Missing priviliges'}), 403
            return f(*args, **kwargs)
        return wrapper
    return validate_role