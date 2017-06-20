from flask import Blueprint, render_template, request, jsonify
import json
from foliumer.mongo import db
from foliumer.models import Page


bp = Blueprint(__name__, __name__, template_folder='templates',
        url_prefix='/pagedata')

@bp.route('/<page_id>', methods=['POST', 'GET'])
def show(page_id):
    page = db.collections.find_one({
        'structure': '#Page',
        'page_id': page_id
    })

    if not page:
        return jsonify({'error': 'No such page'})
    else:
        return jsonify({
            'page_id': page_id,
            '_id': str(page['_id']),
            'editables': page['editables']
        })
