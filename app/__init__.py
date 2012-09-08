from flask import Flask, g
from flask.ext.mako import MakoTemplates
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
import app.config


application = Flask(__name__, template_folder=app.config.TEMPLATE_DIRECTORY)
application.config.from_object('app.config')
MakoTemplates(application)
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)

login_manager = LoginManager()
login_manager.setup_app(application)
