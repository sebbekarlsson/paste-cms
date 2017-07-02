from flask import Blueprint, render_template, request, redirect
from foliumer.mongo import db
from foliumer.models import Page
from foliumer.config import config
from foliumer.utils import login_required
import glob
import ntpath
from bson.objectid import ObjectId
import pymongo


bp = Blueprint(__name__, __name__, template_folder='templates',
        url_prefix='/admin')

@bp.route('/setup', methods=['POST', 'GET'])
def show_setup():
    return render_template('admin/setup.html')

@bp.route('/')
@login_required
def show():
    return render_template('admin/index.html')

@bp.route('/page/<page_id>', methods=['POST', 'GET'])
@login_required
def show_page(page_id):
    page = None

    if page_id != 'new':
        page = db.collections.find_one({
            'structure': '#Page',
            '_id': ObjectId(page_id)
        })

    templates = [
        ntpath.basename(path)
        for path in glob.glob(config['templates_dir'] + '/*.html')
    ]

    if request.method == 'POST':
        page_route = request.form.get('page_route')
        page_template = request.form.get('page_template')
        
        if not page:
            page = Page(page_route=page_route, page_template=page_template)

            res = db.collections.insert_one(page.export())

            return redirect('/admin/page/{}'.format(str(res.inserted_id)))
        else:
            db.collections.update_one({
                'structure': '#Page',
                '_id': page['_id']
            },
            {
                '$set': {
                    'page_route': page_route,
                    'page_template': page_template
                }
            }
            )

            return redirect('/admin/page/{}'.format(str(page['_id'])))
        
    return render_template('admin/page.html', templates=templates, page=page)

@bp.route('/pages', methods=['POST', 'GET'])
@login_required
def show_pages():
    if request.method == 'POST':
        if request.form.get('delete'):
            if request.form.get('page_id'):
                db.collections.remove({
                    'structure': '#Page',
                    '_id': ObjectId(request.form.get('page_id'))
                })

    pages = list(
        db.collections.find({
            'structure': '#Page'
        }).sort('created', pymongo.DESCENDING)
    )

    return render_template('admin/pages.html', pages=pages)

@bp.route('/settings', methods=['POST', 'GET'])
@login_required
def show_settings():
    if request.method == 'POST':
        if request.form.get('delete_all_data'):
            db.collections.remove({})

            return redirect('/admin/setup')

    return render_template('admin/settings.html')
