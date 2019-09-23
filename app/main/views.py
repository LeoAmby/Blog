from flask import render_template, request, redirect, url_for
from . import main
from . import auth
# from .forms import ReviewForm
# from ..models import Revi


@auth.route('/login')
def login():
    return render_template('auth/login.html')