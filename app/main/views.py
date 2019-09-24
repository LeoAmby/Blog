from flask import render_template, request, redirect, url_for
from . import main
from flask_login import login_required
from ..requests import random_quotes


@main.route('/', methods = ['GET', 'POST'])
@login_required
def index():
    quotes = random_quotes()
    return render_template('index.html', quotes = quotes)

@main.route('')
