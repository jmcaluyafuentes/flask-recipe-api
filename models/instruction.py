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
        step_number (int): The sequential order of instructions in cooking process.
        task (str): A specific action that needs to be performed in cooking process.
    """
    __tablename__ = 'instructions'

    id: Mapped[int] = mapped_column(primary_key=True)
    step_number: Mapped[int]
    task: Mapped[str] = mapped_column(Text())
    # recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
