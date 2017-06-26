from flask import Blueprint, render_template, request, jsonify
import json
from foliumer.mongo import db
from foliumer.models import Page


bp = Blueprint(__name__, __name__, template_folder='templates',
        url_prefix='/pagedata')

@bp.route('/<page_route>', methods=['POST', 'GET'])
def show(page_route):
    page = db.collections.find_one({
        'structure': '#Page',
        'page_route': page_route
    })

    if not page:
        return jsonify({'error': 'No such page'})
    else:
        return jsonify({
            'page_route': page_route,
            'page_template': page['page_template'], 
            '_id': str(page['_id']),
            'editables': page['editables']
        })
