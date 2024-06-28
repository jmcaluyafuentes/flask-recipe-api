"""
This module defines SQLAlchemy models and Marshmallow schemas for handling Instruction data.
"""

# Import statements
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey
from init import db, ma

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

    # Set up a relationship and map the recipe_id column as a foreign key to the recipes table
    recipe_id: Mapped[Optional[int]] = mapped_column(ForeignKey('recipes.id'))
    # Establish a relationship between the Recipe and Ingredients models
    recipe: Mapped['Recipe'] = relationship(back_populates='instructions') # type: ignore

class InstructionSchema(ma.Schema):
    """
    Marshmallow schema for serializing and deserializing Instruction objects.
    """
    class Meta:
        """
        Inner class that specifies the fields to include in the schema.
        """
        fields = ('id', 'step_number', 'task')
