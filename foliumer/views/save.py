from flask import Blueprint, render_template, request, jsonify
import json
from foliumer.mongo import db
from foliumer.models import Page


bp = Blueprint(__name__, __name__, template_folder='templates',
        url_prefix='/save')

@bp.route('/', methods=['POST', 'GET'])
def show():
    obj = request.get_json()
    
    if not obj:
        return jsonify({'error': 'No JSON was sent'})

    try:
        obj = json.loads(obj)
    except:
        return jsonify({'error': 'Could not parse Json'})

    if not obj['page_id']:
        return jsonify({'error': 'No page_id was sent'})

    if not obj['editables']:
        return jsonify({'error': 'No editables was sent'})

    existing = db.collections.find_one({
        'structure': '#Page',
        'page_id': obj['page_id']
    })

    resp = None

    if not existing:
        page = Page(**obj)
        resp = db.collections.insert_one(page.export())
    else:
        resp = db.collections.update_one({
            'structure': '#Page',
            'page_id': obj['page_id']
        },
        {
            '$set': obj
        } 
        )

    if resp:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'unknown'})
