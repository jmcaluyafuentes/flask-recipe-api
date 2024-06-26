"""
This module is a blueprint for routes to manage user records.
"""

from datetime import timedelta
from flask import request
from flask import Blueprint
from flask_jwt_extended import create_access_token
from init import db, bcrypt
from auth import admin_only
from models.user import User, UserSchema

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/login', methods=['POST'])
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

@users_bp.route("/", methods=["POST"])
def create_user():
    user_info = UserSchema(only=['email', 'password', 'name', 'is_admin']).load(request.json, unknown='exclude')

    user = User(
        email=user_info['email'],
        password=bcrypt.generate_password_hash(user_info['password']).decode('utf-8'),
        name=user_info.get('name', ''),
        is_admin=user_info.get('is_admin', False)
    )

    db.session.add(user)
    db.session.commit()

    return UserSchema().dump(user), 201
