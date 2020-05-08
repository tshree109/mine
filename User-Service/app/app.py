from flask import Flask
from flask_login import LoginManager, user_loaded_from_header
from user_api import user_api_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
import models

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.init_app(app)


app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@user_db/user',
))

models.init_app(app)
models.create_tables(app)

app.register_blueprint(user_api_blueprint)

SWAGGER_URL = '/api/docs'
API_URL = '/api/user/docs.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id).first()
