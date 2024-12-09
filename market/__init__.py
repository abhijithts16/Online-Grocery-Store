from datetime import timedelta
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "this@is@my@secret"

# Configure database using SQLAlchemy
db_config = yaml.load(open('database.yaml'), Loader=yaml.FullLoader)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_config['mysql_user']}:{db_config['mysql_password']}@{db_config['mysql_host']}/{db_config['mysql_db']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# Initialize SQLAlchemy and Flask-Bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Enabling CSRF protection
csrf = CSRFProtect(app)

@app.after_request
def apply_security_headers(response):
    # Content Security Policy (CSP)
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com; "
        "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
        "font-src 'self' https://cdn.jsdelivr.net; "
        "img-src 'self' data:; "
        "frame-ancestors 'none';"
    )
    # Prevent MIME type sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Clickjacking protection
    response.headers['X-Frame-Options'] = 'DENY'
    # XSS Protection Header (for older browsers)
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

from market import routes