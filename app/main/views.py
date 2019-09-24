from flask import render_template, request, redirect, url_for
from . import main
from flask_login import login_required
from ..requests import requests


@main.route('/', methods = ['GET', 'POST'])
@login_required
def index():
    quotes = requests()
    return render_template('index.html', quotes = quotes)
