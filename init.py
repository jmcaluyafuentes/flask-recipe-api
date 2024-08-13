"""
This module initializes a Flask application with various extensions and configuration settings.
"""

# Import statements
from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Create a base class for all SQLAlchemy models
class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models in the application.
    """
    pass

# Initialize Flask application by creating an instance of Flask class
app = Flask(__name__)

# Set JWT_SECRET_KEY from environment variable JWT_KEY
app.config['JWT_SECRET_KEY'] = environ.get("JWT_KEY")

# Set the database URI from the environment variable
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")

# Initialize SQLAlchemy with the Flask application
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Creating an instance of Marshmallow class and passing in the flask app
ma = Marshmallow(app)

# Initialize Bcrypt extension for password hashing in Flask
bcrypt = Bcrypt(app)

# Initialize JWTManager with the Flask application
jwt = JWTManager(app)

# Port binding for deployment in Render web service
if __name__ == '__main__':
    app.run()
