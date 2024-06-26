"""
This module defines SQLAlchemy models and Marshmallow schemas for handling Recipe data.
"""

# Import statements
from datetime import date
from typing import Optional, List
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
        user_id (int): The foreign key of users table.
        category_id (int): The foreign key of categories table.
    """
    __tablename__ = 'recipes'

    recipe_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text())
    is_public: Mapped[bool] = mapped_column(Boolean, server_default="true")
    preparation_time: Mapped[Optional[int]]
    date_created: Mapped[date]

    # Set up a relationship and map the user_id column as a foreign key to the users table
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    # Establish a relationship between the Recipe and User models
    user: Mapped['User'] = relationship(back_populates='recipes') # type: ignore

    # Set up a relationship and map the category_id column as a foreign key to the categories table
    category_id: Mapped[Optional[int]] = mapped_column(ForeignKey('categories.category_id'))
    # Establish a relationship between the Recipe and Category models
    category: Mapped['Category'] = relationship(back_populates='recipes') # type: ignore

    # Define a one-to-many relationship with ingredient and instructions tables
    ingredients: Mapped[List['Ingredient']] = relationship(back_populates='recipe', cascade="all, delete-orphan") # type: ignore
    instructions: Mapped[List['Instruction']] = relationship(back_populates='recipe', cascade="all, delete-orphan") # type: ignore

class RecipeSchema(ma.Schema):
    """
    Marshmallow schema for serializing and deserializing Recipe objects.
    
    Fields:
        recipe_id (int): The unique identifier for the recipe.
        title (str): The title of the recipe.
        description (str): The description of the recipe.
        is_public (bool): Indicates whether the recipe is public or private.
        preparation_time (int): The time required to prepare the recipe in minutes.
        date_created (date): The date when the recipe was created.
        user (model): The nested record of user model.
        category (model): The nested record of category model.
        ingredients (list): The list of ingredients for the recipe.
        intructions (list): The list of intructions for the recipe.
    """
    user = fields.Nested('UserSchema', exclude=['password'])
    category = fields.Nested('CategorySchema')
    ingredients = fields.Nested('IngredientSchema', many=True)
    instructions = fields.Nested('InstructionSchema', many=True)

    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('recipe_id', 'title', 'description', 'is_public', 'preparation_time', 'date_created', 'user', 'category', 'ingredients', 'instructions')
