from flask import Flask, render_template
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, login_required
import secrets

# Import models and db from models.py
from models import db, User, Role, roles_users

app = Flask(__name__)

# ---------------------------
# Configuration
# ---------------------------
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask-Security settings
app.config['SECURITY_PASSWORD_SALT'] = secrets.token_hex(16)
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_REGISTERABLE'] = False
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

# ---------------------------
# Initialize extensions
# ---------------------------
db.init_app(app)
migrate = Migrate(app, db)

# ---------------------------
# Flask-Security setup
# ---------------------------
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# ---------------------------
# Routes
# ---------------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return "Dashboard placeholder"
