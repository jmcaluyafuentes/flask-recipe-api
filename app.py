from os import environ
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Create a base class for all SQLAlchemy models
class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models in the application.
    """
    pass

# Initialize Flask application by creating an instance of Flask class
app = Flask(__name__)

# Set the database URI from the environment variable
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")

# Initialize SQLAlchemy with the Flask application
db = SQLAlchemy(model_class=Base)

class User(db.Model):
    """
    User model representing the users table in the database.

    Attributes:
        id (int): The primary key for the user.
        username (str): The unique username for the user.
        password_hash (str): The hashed password for the user.
        email (str): The unique email address for the user.
        is_admin (bool): A flag indicating whether the user has admin privileges.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False)

class Category(db.Model):
    """
    Category model representing the categories table in the database.

    Attributes:
        id (int): The primary key for the category.
        name (str): The name of the category, which is non-nullable.
    """
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

class Recipe(db.Model):
    """
    Recipe model representing the recipes table in the database.

    Attributes:
        id (int): The primary key for the recipe.
        title (str): The title of the recipe, which is non-nullable.
        description (str): The description or instructions for the recipe.
        is_public (bool): A flag indicating if the recipe is public or private (default is True).
        preparation_time (int): The time required to prepare the recipe in minutes.
        created_at (datetime): The timestamp when the recipe was created (default is current timestamp).
        updated_at (datetime): The timestamp when the recipe was last updated.
    """
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
    """
    Ingredient model representing the ingredients table in the database.

    Attributes:
        id (int): The primary key for the ingredient.
        name (str): The name of the ingredient, which is non-nullable.
        quantity (str): The quantity of the ingredient, represented as a string (nullable).
    """
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.String(255))

class Instruction(db.Model):
    """
    Instruction model representing the instructions table in the database.

    Attributes:
        id (int): The primary key for the instruction.
        description (str): The description or step of the instruction, which is non-nullable.
        order (int): The order or sequence number of the instruction, which is non-nullable.
    """
    __tablename__ = 'instructions'

    id = db.Column(db.Integer, primary_key=True)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)

class SavedRecipe(db.Model):
    """
    SavedRecipe model representing the saved_recipes table in the database.

    Attributes:
        id (int): The primary key for the saved recipe entry.
        saved_at (datetime): The timestamp when the recipe was saved (default is current timestamp).
        notes (str): Optional notes or comments about the saved recipe.
    """
    __tablename__ = 'saved_recipes'

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    saved_at = db.Column(db.DateTime, default=datetime.now)
    notes = db.Column(db.Text)

@app.cli.command('db_create')
def db_create():
    """
    Custom Flask CLI command to drop and recreate database tables and populate initial data.

    Drops all existing tables, creates new ones based on SQLAlchemy models,
    and adds initial data for users, categories, recipes, ingredients, and instructions.
    """

    # Drop all existing tables
    db.drop_all()

    # Create all tables based on SQLAlchemy models
    db.create_all()

    # Print message confirming table creation
    print('Created tables')

    # Define initial data lists for users, categories, recipes, ingredients, and instructions
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

    # Add initial data to the session
    db.session.add_all(users)
    db.session.add_all(categories)
    db.session.add_all(recipes)
    db.session.add_all(ingredients)
    db.session.add_all(instructions)

    # Commit the session to persist changes to the database
    db.session.commit()

    # saved_recipes = [
    #     SavedRecipe(user_id=user1.id, recipe_id=recipe1.id, notes='Try this with extra cheese.'),
    #     SavedRecipe(user_id=user2.id, recipe_id=recipe2.id, notes='Add more spice for a kick.')
    # ]

    # db.session.add_all(saved_recipes)
    # db.session.commit()

# CLI command to get all users
@app.cli.command("all_users")
def all_users():
    """
    Flask CLI command to fetch and print all users from the database.
    """
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    print(users)

# Command to get all categories
@app.cli.command("all_categories")
def all_categories():
    """
    Flask CLI command to fetch and print all categories from the database.
    """
    stmt = db.select(Category)
    categories = db.session.scalars(stmt).all()
    print(categories)

# Command to get all recipes
@app.cli.command("all_recipes")
def all_recipes():
    """
    Flask CLI command to fetch and print all recipes from the database.
    """
    stmt = db.select(Recipe)
    recipes = db.session.scalars(stmt).all()
    print(recipes)

# Command to get all ingredients
@app.cli.command("all_ingredients")
def all_ingredients():
    """
    Flask CLI command to fetch and print all ingredients from the database.
    """
    stmt = db.select(Ingredient)
    ingredients = db.session.scalars(stmt).all()
    print(ingredients)

# Command to get all instructions
@app.cli.command("all_instructions")
def all_instructions():
    """
    Flask CLI command to fetch and print all instructions from the database.
    """
    stmt = db.select(Instruction)
    instructions = db.session.scalars(stmt).all()
    print(instructions)

# Basic route for the index page to test flask application is working
@app.route('/')
def index():
    """
    Route for the index page.

    Returns:
        str: A simple HTML string for the index page.
    """
    return '<h1>Flask Recipe API</h1>'