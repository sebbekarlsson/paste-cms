import os
from foliumer.app import app
import flask_assets
from flask_assets import Environment, Bundle
import subprocess


def run():
    subprocess.Popen('sass --watch foliumer/static/css/style.scss:foliumer/static/css/style.css',
        shell=True
    )
    
    env = flask_assets.Environment(app)

    # Tell flask-assets where to look for our coffeescript and sass files.
    env.load_path = [
        os.path.join(os.path.dirname(__file__), 'foliumer/static/js')
    ]

    env.register(
        'js_all',
        flask_assets.Bundle(
            'app.js',
            'spinners.js',
            'wpostjs/wpost.js',
            'wgetjs/wget.js',
            'backdrop.js',
            'editables.js',
            'navigation.js',
            filters=['jsmin'],
            output='js/packed.js'
        )
    )

    app.run(debug=True, threaded=True)
