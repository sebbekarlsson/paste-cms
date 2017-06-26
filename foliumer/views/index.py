from flask import Blueprint, render_template
from foliumer.config import config
from foliumer.mongo import db
from foliumer.models import Page


bp = Blueprint(__name__, __name__, template_folder=config['templates_dir'])

@bp.route('/', defaults={'page_route': None})
@bp.route('/<page_route>')
def show(page_route):
    page = None

    if not page_route:
        page_route = ''

    if page_route:
        page = db.collections.find_one({
            'structure': '#Page',
            'page_route': page_route
        })

    if not page and page_route:
        return 'Not Found', 404
    elif not page:
        page = {
            'page_template': 'index.html',
            'page_route': '',
            'editables': []
        }

    return render_template(page['page_template'], page=page)
