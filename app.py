from os import environ
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False)

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    # author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    is_public = db.Column(db.Boolean, default=True)
    # cuisine_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    preparation_time = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.String(255))

class Instruction(db.Model):
    __tablename__ = 'instructions'
    id = db.Column(db.Integer, primary_key=True)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)

class SavedRecipe(db.Model):
    __tablename__ = 'saved_recipes'
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    saved_at = db.Column(db.DateTime, default=datetime.now)
    notes = db.Column(db.Text)

@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    users = [
        User(username='user1', password_hash='hashed_password1', email='user1@example.com'),
        User(username='user2', password_hash='hashed_password2', email='user2@example.com')
    ]

    db.session.add_all(users)
    db.session.commit()

@app.route('/')
def index():
    return '<h1>Flask Recipe API</h1>'