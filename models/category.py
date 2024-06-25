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
        name (str): The name of the category.
    """
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100))

# Marshmallow schema (NOT a db schema)
# Used by Marshmallow to serialize and/or validate our SQLAlchemy models

class CategorySchema(ma.Schema):
    """
    Marshmallow schema for serializing and deserializing Category objects.
    """
    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('id', 'name')
