"""
This module defines a route decorator to ensure that only admin users can access certain routes.
"""

# Import statements
from flask import abort, jsonify, make_response
from flask_jwt_extended import get_jwt_identity
from init import db
from models.user import User

# Ensure that the JWT user is the author of the given recipe
def authorize_owner(recipe):
    """
    Ensure that the JWT user is the author of the given recipe.

    This function checks if the user ID from the JWT payload matches the user ID of the recipe.
    If they do not match, a 403 error is raised.

    Args:
        recipe (Recipe): The recipe object to check ownership against.

    Raises:
        Forbidden: If the JWT user is not the owner of the recipe.
    """
    # Get the user ID from the JWT payload
    user_id = get_jwt_identity()
    if user_id != recipe.user_id:
        abort(make_response(jsonify(error = 'You must be the author of recipe to access this resource'), 403))

def current_user_is_admin():
    """
    Check if the current user is an admin based on their JWT identity.

    Returns:
        bool: True if the current user is an admin, False otherwise.
    """
    # Get the user ID from the JWT payload
    user_id = get_jwt_identity()

    # Query the database to fetch the user and check if it is an admin
    stmt = db.select(User.is_admin).where(User.user_id == user_id)
    is_admin = db.session.scalar(stmt)

    return is_admin