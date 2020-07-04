from flask import Flask
from config import app_config
from flask_migrate import Migrate
from app.models import *
from .admin import admin as admin_blueprint
from .owner import owner as owner_blueprint
from .user import user as user_blueprint
from .auth import auth as auth_blueprint


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(user_blueprint, url_prefix='/user')

    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(owner_blueprint, url_prefix='/owner')
    return app
