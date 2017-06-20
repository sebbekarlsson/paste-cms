from flask import Flask
from foliumer.views.index import bp as index_bp
from foliumer.views.save import bp as save_bp
from foliumer.views.pagedata import bp as pagedata_bp


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(index_bp)
app.register_blueprint(save_bp)
app.register_blueprint(pagedata_bp)
