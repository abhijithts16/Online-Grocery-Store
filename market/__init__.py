from datetime import timedelta
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

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

from market import routes
