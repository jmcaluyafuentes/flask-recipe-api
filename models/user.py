"""
This module defines SQLAlchemy models and Marshmallow schemas for handling User data.
"""

# Import statements
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from init import db, ma

class User(db.Model):
    """
    User model representing the users table in the database.

    Attributes:
        id (int): The primary key for the user.
        username (str): The unique username for the user.
        password (str): The hashed password for the user.
        email (str): The unique email address for the user.
        is_admin (bool): A flag indicating whether the user has admin privileges (default is false).
    """
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True) # Primary key
    email: Mapped[str] = mapped_column(String(200), unique=True) # Email of the user, must be unique
    password: Mapped[str] = mapped_column(String(200)) # Password that will be hashed before storing in database
    name: Mapped[str] = mapped_column(String(100)) # Name of the user, doesn't need to be unique
    is_admin: Mapped[bool] = mapped_column(Boolean, server_default="false") # Is admin flag, defaults to False

class UserSchema(ma.Schema):
    """
    Marshmallow schema for serializing and deserializing User objects.
    
    Fields:
        id (int): The unique identifier for the user.
        email (str): The email address of the user.
        name (str): The name of the user.
        password (str): The hashed password of the user.
        is_admin (bool): Indicates whether the user has admin privileges.
    """
    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('id', 'email', 'name', 'password', 'is_admin')
