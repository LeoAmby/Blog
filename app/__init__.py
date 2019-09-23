from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import config_options
from flask import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = login_manager()

# from app import views

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])


    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from.requests import configure_request
    configure_request(app)

    return app