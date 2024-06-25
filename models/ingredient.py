"""
This module defines SQLAlchemy models and Marshmallow schemas for handling Ingredient data.
"""

# Import statements
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from init import db

class Ingredient(db.Model):
    """
    Ingredient model representing the ingredients table in the database.

    Attributes:
        id (int): The primary key for the ingredient.
        name (str): The name of the ingredient.
        quantity (str): The quantity of the ingredient (optional).
    """
    __tablename__ = 'ingredients'

    id: Mapped[int] = mapped_column(primary_key=True)

    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(200))
    quantity: Mapped[Optional[str]] = mapped_column(String(50))