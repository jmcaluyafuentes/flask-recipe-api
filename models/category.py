"""
This module defines SQLAlchemy models and Marshmallow schemas for handling Category data.
"""

# Import statements
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from init import db, ma

class Category(db.Model):
    """
    Category model representing the categories table in the database.

    Attributes:
        id (int): The primary key for the category.
        cuisine_name (str): The name of the category, particularly the cuisine.
    """
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    cuisine_name: Mapped[str] = mapped_column(String(100))

class CategorySchema(ma.Schema):
    """
    Marshmallow schema for serializing and deserializing Category objects.
    """
    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('id', 'cuisine_name')
