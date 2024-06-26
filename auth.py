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
