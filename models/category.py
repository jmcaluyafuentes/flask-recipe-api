"""
This module defines SQLAlchemy models and Marshmallow schemas for handling Category data.
"""

# Import statements
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from init import db, ma

class Category(db.Model):
    """
    Category model representing the categories table in the database.

    Attributes:
        category_id (int): The primary key for the category.
        cuisine_name (str): The name of the category, particularly the cuisine.
    """
    __tablename__ = 'categories'

    category_id: Mapped[int] = mapped_column(primary_key=True)
    cuisine_name: Mapped[str] = mapped_column(String(100))

    recipes: Mapped[List['Recipe']] = relationship(back_populates='category') # type: ignore

class CategorySchema(ma.Schema):
    """
    Marshmallow schema for serializing and deserializing Category objects.
    """
    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('category_id', 'cuisine_name')
