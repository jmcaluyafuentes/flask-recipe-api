"""
Flask Recipe API

Term 2, Assignment 2
Web Development Accelerated Program
Coder Academy

Student: John Fuentes
"""

# Import statements
from datetime import date, timedelta
from typing import Optional
from flask import request
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError
from init import db, app, bcrypt
from models.user import User, UserSchema
from models.category import Category, CategorySchema
from models.recipe import Recipe, RecipeSchema
from models.ingredient import Ingredient

class Instruction(db.Model):
    """
    Instruction model representing the instructions table in the database.

    Attributes:
        id (int): The primary key for the instruction.
        description (str): The description or step of the instruction.
        order (int): The order or sequence number of the instruction.
    """
    __tablename__ = 'instructions'

    # id = db.Column(db.Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)

    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    description: Mapped[str] = mapped_column(Text())
    order: Mapped[int]

class SavedRecipe(db.Model):
    """
    SavedRecipe model representing the saved_recipes table in the database.

    Attributes:
        id (int): The primary key for the saved recipe entry.
        date_saved (datetime): The timestamp when the recipe was saved (default is current timestamp).
        notes (str): Optional notes or comments about the saved recipe.
    """
    __tablename__ = 'saved_recipes'

    # id = db.Column(db.Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)

    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    date_saved: Mapped[date]
    notes: Mapped[Optional[str]] = mapped_column(Text())

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
        # username & email are unique for each user
        # use bcrypt for slow hashing of password
        User(
            email='admin@example.com', 
            password=bcrypt.generate_password_hash('hashed_password1').decode('utf-8'), 
            is_admin=True
        ),
        User(
            email='user@example.com', 
            password=bcrypt.generate_password_hash('hashed_password2').decode('utf-8'), 
            name='John'
        )
    ]

    categories = [
        Category(name='Italian'),
        Category(name='Mexican')
    ]

    recipes = [
        # description & preparation_time are optional
        # is_public default value is True
        Recipe(title='Spaghetti Carbonara', description='A classic Italian pasta dish.', date_created=date.today(), preparation_time=30),
        Recipe(title='Tacos', date_created=date.today(), is_public=False)
    ]

    ingredients = [
        # quantity is optional
        Ingredient(name='Spaghetti', quantity='200g'),
        Ingredient(name='Eggs', quantity='4'),
        Ingredient(name='Bacon', quantity='100g'),
        Ingredient(name='Tortillas'),
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

# Marshmallow schema (NOT a db schema)
# Used by Marshmallow to serialize and/or validate our SQLAlchemy models

def admin_only(fn):
    """
    Decorator to restrict access to admin users only.

    Returns:
        function: The inner function that performs the admin check and
                either executes the decorated function or returns an
                error message.
    """
    @jwt_required()
    def inner():
        # Ensure the user is an admin
        user_id = get_jwt_identity()
        # Query: Fetch a user based on JWT token subject
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        # Execute query (scalar)
        user = db.session.scalar(stmt)
        # if (user) return users else return error
        if (user):
            return fn()
        else:
            return {'error': 'You must be an admin to access this resource'}, 403    

    return inner

# Routes to get all records
@app.route("/users")
@admin_only
def all_users():
    """
    Route to fetch all users from the database.

    :return: A JSON representation of all user records.
    :rtype: list of dict
    """
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(users)

@app.route("/categories")
def all_categories():
    """
    Route to fetch all categories from the database.

    :return: A JSON representation of all category records.
    :rtype: list of dict
    """
    stmt = db.select(Category)
    categories = db.session.scalars(stmt).all()
    return CategorySchema(many=True).dump(categories)

@app.route("/recipes")
def all_recipes():
    """
    Route to fetch all recipes from the database.

    :return: A JSON representation of all recipe records.
    :rtype: list of dict
    """
    stmt = db.select(Recipe)
    recipes = db.session.scalars(stmt).all()
    return RecipeSchema(many=True).dump(recipes)

# Routes to get a record based on id
@app.route("/users/<int:id>")
def one_user(id):
    """
    Retrieve a user record by its id.

    :param id: The ID of the user to retrieve.
    :type id: int
    :return: A JSON representation of the user record.
    :rtype: dict
    """
    # Fetch the user with the specified ID, or return a 404 error if not found
    user = db.get_or_404(User, id)

    # Serialize the user record to JSON format
    return UserSchema().dump(user)

@app.route("/categories/<int:id>")
def one_category(id):
    """
    Retrieve a category record by its ID.

    :param id: The ID of the category to retrieve.
    :type id: int
    :return: A JSON representation of the category record.
    :rtype: dict
    """
    # Fetch the category with the specified ID, or return a 404 error if not found
    category = db.get_or_404(Category, id)

    # Serialize the category record to JSON format
    return CategorySchema().dump(category)

@app.route("/recipes/<int:id>")
def one_recipe(id):
    """
    Retrieve a recipe record by its ID.

    :param id: The ID of the recipe to retrieve.
    :type id: int
    :return: A JSON representation of the recipe record.
    :rtype: dict
    """
    # Fetch the recipe with the specified ID, or return a 404 error if not found
    recipe = db.get_or_404(Recipe, id)

    # Serialize the recipe record to JSON format
    return RecipeSchema().dump(recipe)

@app.route('/users/login', methods=['POST'])
def login():
    """
    Authenticate a user and generate a JSON Web Token (JWT).

    This endpoint allows a user to log in by providing their email and password. 
    The provided credentials are validated against the stored data in the database. 
    If the credentials are valid, a JWT is generated and returned to the user. 
    If the credentials are invalid, an error message is returned.

    Returns:
        dict: A dictionary containing the JWT if authentication is successful.
        tuple: A dictionary containing an error message and an HTTP status code if authentication fails.
    """
    # Get the email and password from the request
    params = UserSchema(only=['email', 'password']).load(request.json, unknown="exclude")

    # Compare email and password against the database
    stmt = db.select(User).where(User.email == params['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, params['password']):
        # Generate JWT
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=3))
        # Return the JWT
        return {'token': token}
    else:
        # Error handling (user not found, wrong username or password)
        return {'error': 'Invalid email or password'}, 401

# Basic route for the index page to test flask application is working
@app.route('/')
def index():
    """
    Route for the index page.

    Returns:
        str: A simple HTML string for the index page.
    """
    return '<h1>Flask Recipe API</h1>'

@app.errorhandler(404)
def not_found(err):
    """
    Handle 404 Not Found errors.

    This function is called when a 404 error is raised.

    :param err: The error that triggered this handler.
    :type err: Exception
    :return: A JSON response with an error message and a 404 status code.
    :rtype: tuple(dict, int)
    """
    # Return a JSON response with an error message and a 404 status code
    return {'error': 'Not Found'}, 404

@app.errorhandler(405)
def method_not_allowed(err):
    """
    Handle 405 Method Not Allowed errors.

    This function is called when a 405 error is raised.

    :param err: The error that triggered this handler.
    :type err: Exception
    :return: A JSON response with an error message and a 405 status code.
    :rtype: tuple(dict, int)
    """
    # Return a JSON response with an error message and a 404 status code
    return {'error': 'Method Not Allowed'}, 405

@app.errorhandler(KeyError)
def missing_key(err):
    return {"error": f"Missing field: {str(err)}"}

@app.errorhandler(ValidationError)
def invalid_request(err):
    return {"error": vars(err)['messages']}

