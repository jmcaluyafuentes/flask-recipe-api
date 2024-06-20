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

    categories = [
        Category(name='Italian'),
        Category(name='Mexican')
    ]

    recipes = [
        Recipe(title='Spaghetti Carbonara', description='A classic Italian pasta dish.', is_public=True, preparation_time=30),
        Recipe(title='Tacos', description='Delicious Mexican tacos.', is_public=True, preparation_time=20)
    ]

    ingredients = [
        Ingredient(name='Spaghetti', quantity='200g'),
        Ingredient(name='Eggs', quantity='4'),
        Ingredient(name='Bacon', quantity='100g'),
        Ingredient(name='Tortillas', quantity='4'),
        Ingredient(name='Chicken', quantity='200g')
    ]

    instructions = [
        Instruction(description='Boil the spaghetti.', order=1),
        Instruction(description='Fry the bacon.', order=2),
        Instruction(description='Mix eggs with cheese.', order=3),
        Instruction(description='Cook the chicken.', order=1),
        Instruction(description='Assemble the tacos.', order=2)
    ]

    db.session.add_all(users)
    db.session.add_all(categories)
    db.session.add_all(recipes)
    db.session.add_all(ingredients)
    db.session.add_all(instructions)
    db.session.commit()

# Get all users
@app.cli.command("all_users")
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    print(users)

# Get all categories
@app.cli.command("all_categories")
def all_categories():
    stmt = db.select(Category)
    categories = db.session.scalars(stmt).all()
    print(categories)

# Get all recipes
@app.cli.command("all_recipes")
def all_recipes():
    stmt = db.select(Recipe)
    recipes = db.session.scalars(stmt).all()
    print(recipes)

# Get all ingredients
@app.cli.command("all_ingredients")
def all_ingredients():
    stmt = db.select(Ingredient)
    ingredients = db.session.scalars(stmt).all()
    print(ingredients)

# Get all instructions
@app.cli.command("all_instructions")
def all_instructions():
    stmt = db.select(Instruction)
    instructions = db.session.scalars(stmt).all()
    print(instructions)

@app.route('/')
def index():
    return '<h1>Flask Recipe API</h1>'