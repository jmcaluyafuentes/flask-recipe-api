"""
This module is a blueprint for routes to manage user records.
"""

from flask import Blueprint
from init import db
from auth import admin_only
from models.user import User, UserSchema

users_bp = Blueprint('users', __name__, url_prefix='/users')

# Route to get all records
@users_bp.route("/")
@admin_only
def all_users():
    """
    Route to fetch all users from the database.

    :return: A JSON representation of all user records.
    :return_type: list of dict
    """
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(users)

# Route to get a record based on id
@users_bp.route("/<int:user_id>")
def one_user(user_id):
    """
    Retrieve a user record by its id.

    :param id: The ID of the user to retrieve.
    :type id: int
    :return: A JSON representation of the user record.
    :return_type: dict
    """
    # Fetch the user with the specified ID, or return a 404 error if not found
    user = db.get_or_404(User, user_id)

    # Serialize the user record to JSON format
    return UserSchema().dump(user)
