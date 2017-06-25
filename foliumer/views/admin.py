from flask import Blueprint, render_template


bp = Blueprint(__name__, __name__, template_folder='templates',
        url_prefix='/admin')

@bp.route('/')
def show():
    return render_template('admin/index.html')

@bp.route('/page/<page_id>', methods=['POST', 'GET'])
def show_page(page_id):
    if page_id is not 'new':
        # get existing page
        pass

    return render_template('admin/page.html')
