from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import config_options
from app import app


bootstrap = Bootstrap()

from app import views

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])


    bootstrap.init_app(app)


    return app