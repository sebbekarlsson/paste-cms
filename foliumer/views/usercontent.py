from flask import Blueprint, render_template, send_from_directory
from foliumer.config import config
import os


bp = Blueprint(__name__, __name__, template_folder='templates',
        url_prefix='/usercontent')

@bp.route('/<path:filename>')
def show(filename):
    filepath = os.path.join(config['uploads_dir'], filename)

    if not os.path.isfile(filepath):
        return 'Not found', 404

    return send_from_directory(config['uploads_dir'], filename)
