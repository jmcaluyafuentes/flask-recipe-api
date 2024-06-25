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

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(Text())
    is_public: Mapped[bool] = mapped_column(Boolean, server_default="true")
    preparation_time: Mapped[Optional[int]]
    date_created: Mapped[date]
    # author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # cuisine_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

class RecipeSchema(ma.Schema):
    """
    Marshmallow schema for serializing and deserializing Recipe objects.
    """
    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('id', 'title', 'description', 'is_public')
