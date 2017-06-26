from flask import Blueprint, render_template, request
from foliumer.mongo import db
from foliumer.models import Page
from foliumer.config import config
import glob
import ntpath


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

    templates = [
        ntpath.basename(path)
        for path in glob.glob(config['templates_dir'] + '/*.html')
    ]

    if request.method == 'POST':
        page_route = request.form.get('page_route')
        page_template = request.form.get('page_template')

        page = Page(page_route=page_route, page_template=page_template)

        db.collections.insert_one(page.export())

    return render_template('admin/page.html', templates=templates)
