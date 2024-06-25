"""
This module defines SQLAlchemy models and Marshmallow schemas for handling Instruction data.
"""

# Import statements
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from init import db

class Instruction(db.Model):
    """
    Instruction model representing the instructions table in the database.

    Attributes:
        id (int): The primary key for the instruction.
        description (str): The description or step of the instruction.
        order (int): The order or sequence number of the instruction.
    """
    __tablename__ = 'instructions'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text())
    order: Mapped[int]
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
