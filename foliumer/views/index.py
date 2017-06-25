from flask import Blueprint, render_template
from foliumer.config import config
from foliumer.mongo import db
from foliumer.models import Page


bp = Blueprint(__name__, __name__, template_folder=config['templates_dir'])

@bp.route('/', defaults={'page_id': None})
@bp.route('/<page_id>')
def show(page_id):
    page = db.collections.find_one({
        'structure': '#Page',
        'page_id': page_id
    })

    if not page:
        page = {
            'page_id': 'index.html',
            'editables': []
        }

    return render_template(page['page_id'], page=page)
