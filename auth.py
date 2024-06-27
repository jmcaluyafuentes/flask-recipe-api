"""
This module defines a route decorator to ensure that only admin users can access certain routes.
"""

# Import statements
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.user import User

# Route decorator - ensure JWT user is an admin
def admin_only(fn):
    """
    Decorator to restrict access to admin users only.

    Args:
        fn (function): The function to be decorated, which requires admin access.

    Returns:
        function: The inner function that performs the admin check and either
                executes the decorated function or returns an error message.
    
    Raises:
        403 HTTP Error: If the current user is not an admin.
    """
    @jwt_required() # Ensures a valid JWT is present before proceeding
    def inner():
        # Get the user ID from the JWT payload
        user_id = get_jwt_identity()
        # Query the database to fetch the user and check if it is an admin
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        # Execute query (scalar)
        user = db.session.scalar(stmt)
        # Return the decorated function if user is admin, otherwise return an error response
        if (user):
            return fn()
        else:
            return {'error': 'You must be an admin to access this resource'}, 403

    return inner
