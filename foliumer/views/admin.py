from flask import Blueprint, render_template, request, redirect
from foliumer.mongo import db
from foliumer.models import Page, ThemeDBOption, Media
from foliumer.config import config
from foliumer.utils import login_required, is_installed, get_theme_db
import glob
import ntpath
from bson.objectid import ObjectId
import pymongo
import json
import os
from werkzeug.utils import secure_filename


bp = Blueprint(__name__, __name__, template_folder='templates',
        url_prefix='/admin')

@bp.route('/setup', methods=['POST', 'GET'])
def show_setup():
    if is_installed():
        return redirect('/admin')

    existing_index = db.collections.find_one({
        'structure': '#Page',
        'page_route': 'INDEX'
    })

    if not existing_index:
        page = Page(
            page_template='index.html',
            page_route='INDEX',
            editables=[]
        )

        db.collections.insert_one(page.export())

    return render_template('admin/setup.html')

@bp.route('/')
@login_required
def show():
    active_theme = ntpath.basename(config['templates_dir'])
    return render_template('admin/index.html', active_theme=active_theme)

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
                existing = db.collections.find_one({
                    'structure': '#Page',
                    '_id': ObjectId(request.form.get('page_id'))
                })

                if existing:
                    if 'page_route' not in existing:
                        existing['page_route'] = ''

                    if existing['page_route'] != 'INDEX':
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

@bp.route('/user/<user_id>', methods=['POST', 'GET'])
@login_required
def show_user(user_id):
    user = None

    if user_id != 'new':
        user = db.collections.find_one({
            'structure': '#User',
            '_id': ObjectId(user_id)
        })
    
    return render_template('admin/user.html', user=user)

@bp.route('/media', methods=['POST', 'GET'])
@login_required
def show_media():
    if request.method == 'POST':
        if 'upload_file' in request.files:
            file = request.files['upload_file']
            filename = secure_filename(file.filename)

            file.save(os.path.join(config['uploads_dir'], filename))

            media = Media(path=filename)
            db.collections.insert_one(media.export())

    medias = db.collections.find({
        'structure': '#Media'
    })

    return render_template('admin/media.html', medias=medias)

@bp.route('/users', methods=['POST', 'GET'])
@login_required
def show_users():
    users = []

    users = list(db.collections.find({'structure': '#User'}))

    return render_template('admin/users.html', users=users)

@bp.route('/settings', methods=['POST', 'GET'])
@login_required
def show_settings():
    if request.method == 'POST':
        if request.form.get('delete_all_data'):
            db.collections.remove({})

            return redirect('/admin/setup')

    return render_template('admin/settings.html')

@bp.route('/theme-db', methods=['POST', 'GET'])
@login_required
def show_theme_db():
    if request.method == 'POST':
        if request.form.get('empty_db'):
            db.collections.remove({'structure': '#ThemeDBOption'})

    theme_db = get_theme_db()

    if request.method == 'POST':
        if request.form.get('empty_db'):
            db.collections.remove({'structure': '#ThemeDBOption'})

        if request.form.get('save_db'):
            for k in request.form.keys():
                for v in request.form.getlist(k):
                    if 'db_' not in k:
                        continue

                    c_k = k.split('db_')[1]

                    existing = db.collections.find_one({
                        'structure': '#ThemeDBOption',
                        'key': c_k
                    })

                    if not existing:
                        tdbo = ThemeDBOption(
                            key=c_k,
                            value=v
                        )

                        db.collections.insert_one(tdbo.export())
                    else:
                        db.collections.update_one({
                            'structure': '#ThemeDBOption',
                            'key': c_k
                        },
                        {
                            '$set': {'value' : v}
                        }
                        )
        
        theme_db = get_theme_db()

    return render_template('admin/theme_db.html', db=theme_db)
