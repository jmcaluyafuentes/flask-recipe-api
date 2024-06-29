"""
This module is a blueprint for routes to manage user records.
"""

from datetime import timedelta
from flask import request
from flask import Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from init import db, bcrypt
from auth import current_user_is_admin
from models.user import User, UserSchema
from models.recipe import Recipe

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
        token = create_access_token(identity=user.user_id, expires_delta=timedelta(hours=3))
        # Return the JWT
        return {'token': token}
    else:
        # Return an error message if authentication fails
        return {'error': 'Invalid email or password'}, 401

@users_bp.route("/")
@jwt_required()  # Ensure that the request is authenticated using JWT
def get_all_users():
    """
    Route to fetch all users from the database. Accessible only by admin users.

    Returns:
        list of dict: A JSON representation of all user records.
    """
    # Check if the current user is an admin
    if not current_user_is_admin():
        # If not an admin, return a 403 Forbidden error
        return {"error": "Only admin can access this resource"}, 403

    # Create a select statement to fetch all users
    stmt = db.select(User)
    # Execute the query and fetch all user records
    users = db.session.scalars(stmt).all()

    # Return the serialized user data (excluding the password)
    return UserSchema(many=True, exclude=['password']).dump(users)

@users_bp.route("/<int:user_id>")
@jwt_required()  # Ensure that the request is authenticated using JWT
def get_one_user(user_id):
    """
    Retrieve a user record by its ID. Accessible by admin or the user themselves.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A JSON representation of the user record.
    """
    # Get the ID of the current user from the JWT
    current_user_id = get_jwt_identity()

    # Fetch the user with the specified ID, or return a 404 error if not found
    user = db.get_or_404(User, user_id)

    # Check if the current user is not the user themselves and not an admin
    if current_user_id != user.user_id and not current_user_is_admin():
        # If the current user is not authorized, return a 403 Forbidden error
        return {"error": "You are not authorized to access this resource"}, 403

    # Return the serialized user data (excluding the password)
    return UserSchema(exclude=['password']).dump(user)

@users_bp.route("/register", methods=["POST"])
@jwt_required()
def register_user():
    """
    This endpoint handles POST requests to create a new user by an admin. 
    It expects the request body to contain the user's email, password, name, 
    and an optional is_admin flag. The password is hashed before storing it 
    in the database for security reasons.

    Returns:
        tuple: A tuple containing the serialized user data and an HTTP status code.
            - dict: The serialized user data.
            - int: HTTP status code 201 indicating that the user was successfully created.
    """
    # Check if the current user is an admin
    if not current_user_is_admin():
        # If not an admin, return a 403 Forbidden error
        return {"error": "Only admin can register a user"}, 403

    try:
        # Load and validate the incoming user data against the UserSchema
        user_info = UserSchema(only=['email', 'password', 'name', 'is_admin']).load(request.json, unknown='exclude')
        # Create a new User instance with the provided data
        user = User(
            email=user_info['email'],
            password=bcrypt.generate_password_hash(user_info['password']).decode('utf-8'),
            name=user_info['name'],
            is_admin=user_info.get('is_admin', False)
        )
        # Add the new user to the database session
        db.session.add(user)
        # Commit the session to save the new user to the database
        db.session.commit()
        # Return the serialized user data (excluding the password) and a 201 Created status code
        return UserSchema(exclude=['password']).dump(user), 201
    

    except IntegrityError:
        # Rollback the session if there is an integrity error (e.g., email already exists)
        db.session.rollback()
        # Return a 400 Bad Request error with a message indicating the issue
        return {"error": "The email address already exists. Please choose a different email address."}, 400

    except SQLAlchemyError:
        # Rollback the session if there is a general SQLAlchemy error other than the IntegrityError
        db.session.rollback()
        # Return a 500 Internal Server Error with a generic error message
        return {"error": "An error occurred while creating the user."}, 500

@users_bp.route("/<int:user_id>", methods=["PUT", "PATCH"])
@jwt_required()  # Ensure that the request is authenticated using JWT
def update_user(user_id):
    """
    Endpoint to update an existing user. Accessible by admin or the user themselves.

    Args:
        user_id (int): The ID of the user to be updated.

    Returns:
        tuple: A tuple containing the serialized updated user data and an HTTP status code.
            - dict: The serialized updated user data.
            - int: HTTP status code 200 indicating that the user was successfully updated.
    """
    # Get the ID of the current user from the JWT
    current_user_id = get_jwt_identity()

    # Fetch the user with the specified ID, or return a 404 error if not found
    user = db.get_or_404(User, user_id)

    # Check if the current user is not the user themselves and not an admin
    if current_user_id != user.user_id and not current_user_is_admin():
        # If the current user is not authorized, return a 403 Forbidden error
        return {"error": "You are not authorized to access this resource"}, 403

    try:
        # Load the request data and validate it against the UserSchema
        user_info = UserSchema(only=['email', 'password', 'name', 'is_admin']).load(request.json, unknown='exclude')

        # Update the user fields if new values are provided, otherwise keep the existing values
        user.email = user_info.get('email', user.email)
        if 'password' in user_info:
            user.password = bcrypt.generate_password_hash(user_info['password']).decode('utf-8')
        user.name = user_info.get('name', user.name)
        
        # Only allow admins to update the is_admin field
        if current_user_is_admin():
            user.is_admin = user_info.get('is_admin', user.is_admin)
        
        # Commit the updated user to the database
        db.session.commit()

        # Return the serialized updated user data
        return UserSchema().dump(user)
    
    except IntegrityError:
        # Rollback the session to undo any partial changes due to an integrity constraint violation
        db.session.rollback()
        # Return an error message indicating that the email address already exists with a 400 Bad Request status code
        return {"error": "The email address already exists. Please choose a different email address."}, 400

    except SQLAlchemyError:
        # Rollback the session to undo any partial changes due to a general SQLAlchemy error
        db.session.rollback()
        # Return a generic error message indicating a database error with a 500 Internal Server Error status code
        return {"error": "An error occurred while updating the user."}, 500

@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()  # Ensure that the request is authenticated using JWT
def delete_user(user_id):
    """
    Endpoint to delete an existing user. Accessible by admin or the user themselves.

    This function deletes a user and all their associated recipes from the database.
    It ensures that the action is authorized by allowing only the user themselves or an admin 
    to perform the deletion.

    Args:
        user_id (int): The ID of the user to be deleted.

    Returns:
        dict: An empty dictionary indicating successful deletion.
            - {}: A response indicating that the user and their recipes were successfully deleted.
            - int: HTTP status code 200 indicating success.
            - int: HTTP status code 403 if the user is not authorized.
            - int: HTTP status code 500 if an error occurred while deleting the user or their recipes.
    """
    # Get the ID of the current user from the JWT
    current_user_id = get_jwt_identity()

    # Fetch the user with the specified ID, or return a 404 error if not found
    user = db.get_or_404(User, user_id)

    # Check if the current user is not the user themselves and not an admin
    if current_user_id != user.user_id and not current_user_is_admin():
        # If the current user is not authorized, return a 403 Forbidden error
        return {"error": "You are not authorized to access this resource."}, 403

    try:
        # Fetch and delete all recipes associated with the user
        recipes = Recipe.query.filter_by(user_id=user.user_id).all()
        for recipe in recipes:
            db.session.delete(recipe)
        
        # Delete the user from the database
        db.session.delete(user)
        # Commit the changes to the database
        db.session.commit()
        # Return an empty dictionary to signify successful deletion
        return {}, 200
    
    except SQLAlchemyError:
        # Rollback the session to undo any partial changes due to a general SQLAlchemy error
        db.session.rollback()
        # Return a generic error message indicating a database error with a 500 Internal Server Error status code
        return {"error": "An error occurred while deleting the user."}, 500
