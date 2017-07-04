from flask import Blueprint, render_template, request, jsonify
import json
from foliumer.mongo import db
from foliumer.models import User, Option
from foliumer.utils import is_installed


bp = Blueprint(__name__, __name__, template_folder='templates',
        url_prefix='/api')

@bp.route('/install', methods=['POST', 'GET'])
def show():
    if is_installed():
        return jsonify({'error': 'Already installed'}), 400

    obj = request.get_json()

    if not obj:
        return jsonify({'error': 'No data sent'}), 400

    try:
        obj = json.loads(obj)
    except:
        return jsonify({'error': 'Could not parse json'}), 400

    if 'admin' in obj:
        # user tries to register an administrator

        admin = obj['admin']
        
        if not 'username' in admin:
            return jsonify({'error': 'Missing username in admin'}), 400

        if not 'password' in admin:
            return jsonify({'error': 'Missing password in admin'}), 400

        if not 'password_confirm' in admin:
            return jsonify({'error': 'Missing confirmation password in admin'}), 400

        if not admin['username']:
            return jsonify({'error': 'Invalid username'}), 400

        if not admin['password']:
            return jsonify({'error': 'Invalid password'}), 400

        if not admin['password_confirm']:
            return jsonify({'error': 'Invalid confirmation password'}), 400

        if admin['password'] != admin['password_confirm']:
            return jsonify({'error': 'Passwords does not match!'}), 400

        if len(admin['username']) < 3:
            return jsonify({'error': 'Username needs to be at least 3 characters'})

        if len(admin['password']) < 3:
            return jsonify({'error': 'Password needs to be at least 3 characters'})

        user = User(username=admin['username'], password=admin['password'])
        option = Option(key='cms_installed', value=True)

        db.collections.insert_one(user.export())
        db.collections.insert_one(option.export())

        return jsonify({'message': 'All good'}), 200

    return jsonify({'error': 'Unknown operation'}), 400
