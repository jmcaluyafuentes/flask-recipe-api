"""
Flask Recipe API

Term 2, Assignment 2
Web Development Accelerated Program
Coder Academy

Student: John Fuentes
"""

# Import statements
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError
from flask import render_template_string
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

    html_content = '''
        <h1>Flask Recipe API</h1>
        <h3>Term 2 Assignment</h3>
        <h3>Coder Academy, Diploma of IT</h3>
        <p>For detailed documentation on available endpoints, visit the <a href="https://github.com/jmcaluyafuentes/flask-recipe-api/tree/master" target="_blank">GitHub repository</a>.</p>
        <p>Use API clients like Postman or Bruno to test the endpoints.</p>
    '''
    return render_template_string(html_content)

@app.errorhandler(404)
def not_found(_):
    """
    This function is called when a 404 error is raised.

    Args:
        _ (Exception): The exception that triggered this handler. Placeholder parameter (unused).

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
        _ (Exception): The exception that triggered this handler. Placeholder parameter (unused).
 
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

# @app.errorhandler(IntegrityError)
# def integrity_error(_):
#     """
#     This function is called when an IntegrityError is raised,
#     due to a violation of a database integrity constraint,
#     such as a unique constraint violation.

#     Args:
#         _ (Exception): The exception that triggered this handler. Placeholder parameter (unused).

#     Returns:
#         tuple: A JSON response containing the error message and the HTTP status code 400.
#     """
#     return {'error': 'The provided title already exists. Please choose a different title.'}, 400

@app.errorhandler(IntegrityError)
def handle_integrity_error(err):
    """
    Error handler for IntegrityError exceptions.

    Args:
        e (Exception): The IntegrityError exception raised.

    Returns:
        tuple: A tuple containing a dictionary with error messages and an integer
            representing the HTTP status code (400).
    """
    # Get the original error message
    error_message = str(err.orig)

    if 'unique constraint' in error_message.lower():
        # Extracting the field name causing the violation from the error message
        field_name = error_message.split('(')[-1].split(')')[0]

        # Return a JSON response with the specific field causing the error
        return {'error': f'{field_name} already exists. Please choose a different value.'}, 400
    else:
        # Return a generic error message for other IntegrityError cases
        return {'error': 'Database integrity error', 'message': str(err.orig)}, 400

# Print all routes with endpoints that are registered in the app
print(app.url_map)
