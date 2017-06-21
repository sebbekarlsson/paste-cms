from flask import Blueprint, render_template


bp = Blueprint(__name__, __name__, template_folder='templates',
        url_prefix='/admin')

@bp.route('/')
def show():
    return render_template('admin/index.html')
