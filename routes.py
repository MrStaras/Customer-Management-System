from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, Client

#1. Define the Blueprint
main_bp = Blueprint('main', __name__)

#2. Define dashboard route
@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)
