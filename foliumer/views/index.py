from flask import Blueprint, render_template
from foliumer.mongo import db


bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/<page_id>')
def show(page_id):
    page = db.collections.find_one({
        'structure': '#Page',
        'page_id': page_id
    })

    return render_template('testing/startpage.html', page=page)
