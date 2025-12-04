from flask import Flask, redirect, url_for
from flask_login import LoginManager
from config import Config
from models import db, User
from auth import auth_bp
from routes import main_bp

#1. Initialize Flask application and load configuration
app = Flask(__name__)
app.config.from_object('config.Config')

#2. Initialize database and Login Manager
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#3. Register authentication blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

#4 . Define root route to redirect to main page
@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)



