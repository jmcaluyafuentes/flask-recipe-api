"""
This module defines SQLAlchemy models and Marshmallow schemas for handling Recipe data.
"""

# Import statements
from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Text, ForeignKey
from marshmallow import fields
from init import db, ma

class Recipe(db.Model):
    """
    Recipe model representing the recipes table in the database.

    Attributes:
        id (int): The primary key for the recipe.
        title (str): The unique title of the recipe.
        description (str): The description for the recipe (optional).
        is_public (bool): A flag indicating if the recipe is public or private (default is True for public).
        preparation_time (int): The time required to prepare the recipe in minutes (optional).
        date_created (date): The timestamp when the recipe was created.
    """
    __tablename__ = 'recipes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text())
    is_public: Mapped[bool] = mapped_column(Boolean, server_default="true")
    preparation_time: Mapped[Optional[int]]
    date_created: Mapped[date]

    # Set up a relationship in SQLAlchemy and map it to a user
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='recipes') # type: ignore

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
    user = fields.Nested('UserSchema', exclude=['password'])

    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('id', 'title', 'description', 'is_public', 'preparation_time', 'date_created', 'user')
