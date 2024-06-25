"""
This module defines SQLAlchemy models and Marshmallow schemas for handling SavedRecipe data.
"""

# Import statements
from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from init import db

class SavedRecipe(db.Model):
    """
    SavedRecipe model representing the saved_recipes table in the database.

    Attributes:
        id (int): The primary key for the saved recipe entry.
        date_saved (datetime): The timestamp when the recipe was saved (default is current timestamp).
        notes (str): Optional notes or comments about the saved recipe.
    """
    __tablename__ = 'saved_recipes'

    id: Mapped[int] = mapped_column(primary_key=True)
    date_saved: Mapped[date]
    notes: Mapped[Optional[str]] = mapped_column(Text())
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)