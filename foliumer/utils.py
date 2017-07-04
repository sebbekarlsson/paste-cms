from flask import session, redirect, request
from foliumer.mongo import db
from foliumer.config import config
from functools import wraps
import json
from bson.objectid import ObjectId


def is_installed():
    option = db.collections.find_one({
        'structure': '#Option',
        'key': 'cms_installed'
    })

    if not option:
        return False

    return option['value']

def get_current_user():
    if 'user_id' not in session:
        return None

    return db.collections.find_one({
        'structure': '#User',
        '_id': ObjectId(str(session['user_id']))
    })

def is_loggedin():
    return get_current_user() is not None

def installed_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_installed():
            return redirect('/admin/setup')
        return f(*args, **kwargs)
    return decorated_function

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not get_current_user():
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

def editable_area(id=0, page_route=None):
    _page_route = ''
    html = ''

    _page_route = 'INDEX'
    
    if page_route:
        _page_route = page_route
    elif request.path and request.path != '':
        _page_route = request.path

    if '/' in _page_route:
        _page_route = _page_route.split('/')[1]

    if _page_route == '/' or _page_route == '':
        _page_route = 'INDEX'

    page = db.collections.find_one({
        'structure': '#Page',
        'page_route': _page_route
    })

    if not page:
        page = {
            'page_template': 'index.html',
            'route': 'INDEX',
            'editables': []
        }

    if not is_loggedin():
        for editable in page['editables']:
            if editable['editable_id'] == id:
                return editable['text']

    if page_route:
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

def get_theme_db():
    theme_db = {}

    try:
        with open(config['templates_dir'] + '/db.json') as jfile:
            theme_db = json.loads(jfile.read())
        jfile.close()
    except:
        pass

    m_db = list(db.collections.find({
        'structure': '#ThemeDBOption'
    }))

    for mopt in m_db:
        if mopt['key'] in theme_db:
            theme_db[mopt['key']] = mopt['value']


    return theme_db
