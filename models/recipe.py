"""
This module defines SQLAlchemy models and Marshmallow schemas for handling Recipe data.
"""

# Import statements
from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Text
from init import db, ma

class Recipe(db.Model):
    """
    Recipe model representing the recipes table in the database.

    Attributes:
        id (int): The primary key for the recipe.
        title (str): The title of the recipe.
        description (str): The description for the recipe (optional).
        is_public (bool): A flag indicating if the recipe is public or private (default is True for public).
        preparation_time (int): The time required to prepare the recipe in minutes (optional).
        date_created (date): The timestamp when the recipe was created.
    """
    __tablename__ = 'recipes'

    id: Mapped[int] = mapped_column(primary_key=True) # Primary key
    title: Mapped[str] = mapped_column(String(200), unique=True) # Title of the recipe, must be unique
    description: Mapped[Optional[str]] = mapped_column(Text()) # Description of the recipe, optional
    is_public: Mapped[bool] = mapped_column(Boolean, server_default="true") # Public visibility flag, defaults to True
    preparation_time: Mapped[Optional[int]] # Preparation time in minutes, optional
    date_created: Mapped[date] # Date when the recipe was created
    
    # Foreign key columns
    # author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # cuisine_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

class RecipeSchema(ma.Schema):
    """
    Marshmallow schema for serializing and deserializing Recipe objects.
    
    Fields:
        id (int): The unique identifier for the recipe.
        title (str): The title of the recipe.
        description (str): The description of the recipe.
        is_public (bool): Indicates whether the recipe is public or private.
        preparation_time (int): The time required to prepare the recipe in minutes.
        date_created (date): The date when the recipe was created.
    """
    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('id', 'title', 'description', 'is_public', 'preparation_time', 'date_created')
