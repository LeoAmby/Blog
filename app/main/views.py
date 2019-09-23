from flask import render_template, request, redirect, url_for
from . import main
from flask_login import login_required



@main.route('/', methods = ['GET', 'POST'])
@login_required
def new_tale(id):