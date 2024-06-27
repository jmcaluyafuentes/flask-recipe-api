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

# Define a blueprint for user-related routes
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

    # Query the database for a user with the provided email
    stmt = db.select(User).where(User.email == params['email'])

    # Execute the query and fetch the scalar result (single row), if any.
    user = db.session.scalar(stmt)

    # Check if the user exists and if the password is correct
    if user and bcrypt.check_password_hash(user.password, params['password']):
        # Generate a JWT with a 3-hour expiration time
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=3))
        # Return the JWT
        return {'token': token}
    else:
        # Return an error message if authentication fails
        return {'error': 'Invalid email or password'}, 401

@users_bp.route("/")
@admin_only
def all_users():
    """
    Route to fetch all users from the database.
    It is restricted to admin users only.

    Returns:
        list of dict: A JSON representation of all user records.
    """
    # Query the database for all user records
    stmt = db.select(User)
    # Execute the query and fetch all users
    users = db.session.scalars(stmt).all()

    # Return the serialized users
    return UserSchema(many=True).dump(users)

@users_bp.route("/<int:user_id>")
def one_user(user_id):
    """
    Retrieve a user record by its ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A JSON representation of the user record.
    """
    # Fetch the user with the specified ID, or return a 404 error if not found
    user = db.get_or_404(User, user_id)

    # Return the serialized user
    return UserSchema().dump(user)

@users_bp.route("/", methods=["POST"])
def create_user():
    """
    This endpoint handles POST requests to create a new user. It expects the request 
    body to contain the user's email, password, name, and an optional is_admin flag.
    The password is hashed before storing it in the database for security reasons.

    Returns:
        tuple: A tuple containing the serialized user data and an HTTP status code.
            - dict: The serialized user data.
            - int: HTTP status code 201 indicating that the user was successfully created.

    Raises:
        ValidationError: If the input data does not conform to the expected schema.
        KeyError: If there is a missing field.
    """
    # Load the request data and validate it against the UserSchema
    user_info = UserSchema(only=['email', 'password', 'name', 'is_admin']).load(request.json, unknown='exclude')

    # Create a new user instance
    user = User(
        email=user_info['email'],
        password=bcrypt.generate_password_hash(user_info['password']).decode('utf-8'),
        name=user_info['name'],
        is_admin=user_info.get('is_admin', False)
    )

    # Add the new user to the session and commit it to the database
    db.session.add(user)
    db.session.commit()

    # Return the serialized recipe data and a 201 Created status code
    return UserSchema().dump(user), 201

@users_bp.route("/<user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    """
    Endpoint to update an existing user.

    This function handles PUT and PATCH requests to update an existing user by their ID.
    It expects the request body to contain one or more fields of the user that need to be updated,
    including email, password, name, and is_admin flag. Any fields not provided in the request will remain unchanged.

    Args:
        user_id (int): The ID of the user to be updated.

    Returns:
        tuple: A tuple containing the serialized updated user data and an HTTP status code.
            - dict: The serialized updated user data.
            - int: HTTP status code 200 indicating that the user was successfully updated.

    Raises:
        ValidationError: If the input data does not conform to the expected schema.
        NotFound: If the user with the given ID does not exist.
    """
    # Fetch the user with the specified ID, or return a 404 error if not found
    user = db.get_or_404(User, user_id)
    # Load the request data and validate it against the UserSchema
    user_info = UserSchema(only=['email', 'password', 'name', 'is_admin']).load(request.json, unknown='exclude')
    
    # Update the recipe fields if new values are provided, otherwise keep the existing values
    user.email = user_info.get('email', user.email)
    user.password = user_info.get(bcrypt.generate_password_hash('password').decode('utf-8'), user.password)
    user.name = user_info.get('name', user.name)
    user.admin = user_info.get('is_admin', user.is_admin)

    # Commit the updated user to the database
    db.session.commit()

    # Return the serialized updated user data
    return UserSchema().dump(user)
