from flask import session, redirect, request
from foliumer.mongo import db
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

def editable_area(id=0, page_route=None):
    if page_route:
        page = db.collections.find_one({
            'structure': '#Page',
            'page_route': page_route
        })
        
        if request.path != page_route and not (page_route == 'INDEX' and request.path == '/'):
            for editable in page['editables']:
                if editable['editable_id'] == id:
                    if is_loggedin():
                        page_route = page_route.replace('INDEX', '/')

                        return editable['text'] + '<a href="{}">Edit<a>'.format(page_route)
                    else:
                        return editable['text']

    return """<div class='admin-editable' data-editable-type='text' data-editable-id='IDENTIFIER'>
        </div>""".replace('IDENTIFIER', id)