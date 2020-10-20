# Import flask and template operators
from flask import Flask

# Import Peewee
from config import DATABASE
from peewee import SqliteDatabase

from flask_login import LoginManager

# Define the WSGI application object
suamascara = Flask(__name__)

# CSRF
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
csrf.init_app(suamascara)


# Configurations
suamascara.config.from_object('config')


# Define the database object which is imported
# by modules and controllers
db = SqliteDatabase(DATABASE)

l_m = LoginManager()
l_m.init_app(suamascara)

from app.models.tables import User, Mascara

db.create_tables ([User, Mascara])

from app.controllers import views