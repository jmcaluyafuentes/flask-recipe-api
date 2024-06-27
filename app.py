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
    Renders the index page of the Flask Recipe API.
    This route serves as a basic test to check if the Flask application is operational.

    Returns:
        str: HTML content displaying a heading for the index page.
    """
    return '<h1>Flask Recipe API</h1>'

@app.errorhandler(404)
def not_found(_):
    """
    This function is called when a 404 error is raised.

    Args:
        _: Placeholder parameter (unused).

    Returns:
        tuple: A JSON response with an error message and a 404 status code.
            The tuple consists of a dictionary containing the error message
            and an integer representing the HTTP status code.
    """
    return {'error': 'Not Found'}, 404

@app.errorhandler(405)
def method_not_allowed(_):
    """
    This function is called when a 405 error is raised.

    Args:
        _: Placeholder parameter (unused).

    Returns:
        tuple: A tuple containing a dictionary with an error message and an integer 
            representing the HTTP status code (405).
    """
    return {'error': 'Method Not Allowed'}, 405

@app.errorhandler(KeyError)
def missing_key(err):
    """
    This function handles KeyError exceptions by returning a JSON response
    with an error message indicating the missing field.

    Args:
        err (KeyError): The KeyError exception that was raised.

    Returns:
        tuple: A tuple containing a dictionary with an error message indicating
            the missing field and an integer representing the HTTP status code (400).
    """
    return {"error": f"Missing field: {str(err)}"}, 400

@app.errorhandler(ValidationError)
def invalid_request(err):
    """
    This function handles ValidationError exceptions by returning a JSON response
    with an error message indicating the validation errors.

    Args:
        err (ValidationError): The ValidationError exception that was raised.

    Returns:
        tuple: A tuple containing a dictionary with the validation error messages and an integer
            representing the HTTP status code (400).
    """
    return {"error": vars(err)['messages']}, 400

# Print all routes with endpoints that are registered in the app
print(app.url_map)
