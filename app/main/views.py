from flask import render_template, request, redirect, url_for
from . import main
from flask_login import login_required


@main.route('/', methods = ['GET', 'POST'])
@login_required
def index():
    # posts = Post.query.all()
    return render_template('index.html')
