from flask import Blueprint, render_template, request, session, redirect
from foliumer.config import config
from foliumer.utils import is_loggedin, installed_required


bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/login', methods=['POST', 'GET'])
@installed_required
def show():
    errors = []

    if request.method == 'POST':
        login_username = request.form.get('login_username')
        login_password = request.form.get('login_password')

        if login_username != config['admin']['username']:
            errors.append('Wrong credentials')

        if login_password != config['admin']['password']:
            errors.append('Wrong credentials')

        if len(errors) == 0:
            session['user_id'] = 'admin'

    if is_loggedin():
        return redirect('/admin')

    return render_template('admin/login.html', errors=errors)

@bp.route('/logout', methods=['POST', 'GET'])
@installed_required
def show_logout():
    session['user_id'] = None
    del session['user_id']

    return redirect('/')
