from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from models import User # To check if user exists

#1. Create Blueprint for authentication
auth_bp = Blueprint('auth', __name__)

#2. Define login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 1. Get email (not username) from the form
        email = request.form.get('email')  
        password = request.form.get('password')

        # 2. Validate user credentials using email
        user = User.query.filter_by(email=email).first()  

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password') 
                
    #3. Render login template
    return render_template('login.html')

#4. Define logout route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
