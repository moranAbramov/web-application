from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import secrets

# Construct the core application
app = Flask(__name__)
app.config.from_object(Config)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = secrets.token_hex(16)
db = SQLAlchemy(app)


from api import routes
