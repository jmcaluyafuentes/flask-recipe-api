"""
This module defines SQLAlchemy models and Marshmallow schemas for handling Ingredient data.
"""

# Import statements
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from init import db, ma

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
    name: Mapped[str] = mapped_column(String(200))
    quantity: Mapped[Optional[str]] = mapped_column(String(50))
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)

    # Set up a relationship and map the recipe_id column as a foreign key to the recipes table
    recipe_id: Mapped[Optional[int]] = mapped_column(ForeignKey('recipes.id'))
    # Establish a relationship between the Recipe and Ingredients models
    recipe: Mapped['Recipe'] = relationship(back_populates='ingredients') # type: ignore

class IngredientSchema(ma.Schema):
    """
    Marshmallow schema for serializing and deserializing Ingredient objects.
    """
    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('id', 'name', 'quantity')
