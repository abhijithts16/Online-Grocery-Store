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

# Initialize SQLAlchemy and Flask-Bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
