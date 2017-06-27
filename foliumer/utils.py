from flask import session, redirect
from functools import wraps


def get_current_user():
    if 'user_id' not in session:
        return None

    return {'_id': session['user_id']}

def is_loggedin():
    return get_current_user() is not None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not get_current_user():
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
