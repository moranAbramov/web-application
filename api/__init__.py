from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


# Construct the core application
app = Flask(__name__)
app.config.from_object(Config)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "moran abramov"  # CHANGE THIS LINE
db = SQLAlchemy(app)


from api import routes
