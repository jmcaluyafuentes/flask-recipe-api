"""
Flask Recipe API

Term 2, Assignment 2
Web Development Accelerated Program
Coder Academy

Student: John Fuentes
"""

# Import statements
from datetime import timedelta
from flask import request
from flask_jwt_extended import create_access_token
from marshmallow.exceptions import ValidationError
from init import db, app, bcrypt
from models.user import User, UserSchema
from models.category import Category, CategorySchema
from models.recipe import Recipe, RecipeSchema
# from models.ingredient import Ingredient
# from models.instruction import Instruction
# from models.saved_recipe import SavedRecipe
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)

# Route to get all records
@app.route("/categories")
def all_categories():
    """
    Route to fetch all categories from the database.

    :return: A JSON representation of all category records.
    :return_type: list of dict
    """
    stmt = db.select(Category)
    categories = db.session.scalars(stmt).all()
    return CategorySchema(many=True).dump(categories)

@app.route("/recipes")
def all_recipes():
    """
    Route to fetch all recipes from the database.

    :return: A JSON representation of all recipe records.
    :return_type: list of dict
    """
    stmt = db.select(Recipe)
    recipes = db.session.scalars(stmt).all()
    return RecipeSchema(many=True).dump(recipes)

# Route to get a record based on id
@app.route("/categories/<int:cat_id>")
def one_category(cat_id):
    """
    Retrieve a category record by its ID.

    :param id: The ID of the category to retrieve.
    :type id: int
    :return: A JSON representation of the category record.
    :return_type: dict
    """
    # Fetch the category with the specified ID, or return a 404 error if not found
    category = db.get_or_404(Category, cat_id)

    # Serialize the category record to JSON format
    return CategorySchema().dump(category)

@app.route("/recipes/<int:recipe_id>")
def one_recipe(recipe_id):
    """
    Retrieve a recipe record by its ID.

    :param id: The ID of the recipe to retrieve.
    :type id: int
    :return: A JSON representation of the recipe record.
    :return_type: dict
    """
    # Fetch the recipe with the specified ID, or return a 404 error if not found
    recipe = db.get_or_404(Recipe, recipe_id)

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
        tuple: A dictionary containing an error message
            and an HTTP status code if authentication fails.
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
    :return_type: tuple(dict, int)
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
    :return_type: tuple(dict, int)
    """
    # Return a JSON response with an error message and a 404 status code
    return {'error': 'Method Not Allowed'}, 405

@app.errorhandler(KeyError)
def missing_key(err):
    """
    This function handles KeyError exceptions by returning a JSON response
    with an error message indicating the missing field.

    :param err: The KeyError exception that was raised.
    :type err: KeyError
    :return: A JSON response with an error message indicating the missing field.
    :return_type: dict
    """
    return {"error": f"Missing field: {str(err)}"}

@app.errorhandler(ValidationError)
def invalid_request(err):
    """
    This function handles ValidationError exceptions by returning a JSON response
    with an error message indicating the validation errors.

    :param err: The ValidationError exception that was raised.
    :type err: ValidationError
    :return: A JSON response with the validation error messages.
    :return_type: dict
    """
    return {"error": vars(err)['messages']}

