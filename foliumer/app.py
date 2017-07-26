from flask import Flask
from foliumer.views.api import bp as api_bp
from foliumer.views.index import bp as index_bp
from foliumer.views.save import bp as save_bp
from foliumer.views.pagedata import bp as pagedata_bp
from foliumer.views.login import bp as login_bp
from foliumer.views.admin import bp as admin_bp
from foliumer.views.usercontent import bp as usercontent_bp
from foliumer.config import config
from foliumer.utils import is_loggedin, get_current_user, editable_area
from foliumer.mongo import db


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(api_bp)
app.register_blueprint(index_bp)
app.register_blueprint(save_bp)
app.register_blueprint(pagedata_bp)
app.register_blueprint(login_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(usercontent_bp)

app.add_template_global(config, name='config')
app.add_template_global(db, name='mongo')
app.add_template_global(is_loggedin, name='is_loggedin')
app.add_template_global(get_current_user, name='get_current_user')
app.add_template_global(editable_area, name='editable_area')
