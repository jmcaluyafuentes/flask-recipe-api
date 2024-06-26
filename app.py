"""
Flask Recipe API

Term 2, Assignment 2
Web Development Accelerated Program
Coder Academy

Student: John Fuentes
"""

# Import statements
from marshmallow.exceptions import ValidationError
from init import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.categories_bp import categories_bp
from blueprints.recipes_bp import recipes_bp

# Register the blueprints with the Flask application
app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(recipes_bp)

@app.route('/')
def index():
    """
    Route for the index page.

    Returns:
        str: A simple HTML string for the index page.
    """
    return '<h1>Flask Recipe API</h1>'

@app.errorhandler(404)
def not_found(_):
    """
    Handle 404 Not Found errors.

    This function is called when a 404 error is raised.

    :param _: Placeholder parameter (unused).
    :return: A JSON response with an error message and a 404 status code.
    :return_type: tuple(dict, int)
    """
    return {'error': 'Not Found'}, 404

@app.errorhandler(405)
def method_not_allowed(_):
    """
    Handle 405 Method Not Allowed errors.

    This function is called when a 405 error is raised.

    :param _: Placeholder parameter (unused).
    :return: A JSON response with an error message and a 405 status code.
    :return_type: tuple(dict, int)
    """
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
    return {"error": f"Missing field: {str(err)}"}, 400

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
    return {"error": vars(err)['messages']}, 400

@app.errorhandler(ValueError)
def invalid_salt(err):
    """
    Handle ValueError exceptions related to invalid salt.

    This function is called when a ValueError is raised, specifically for invalid salt errors.

    :param err: The ValueError exception that was raised.
    :type err: ValueError
    :return: A JSON response with an error message indicating the invalid salt error.
    :return_type: tuple(dict, int)
    """
    if 'Invalid salt' in str(err):
        return {"error": "Invalid salt"}, 400
    return {"error": str(err)}, 400

# Print all routes with endpoints that are registered in the app
print(app.url_map)
