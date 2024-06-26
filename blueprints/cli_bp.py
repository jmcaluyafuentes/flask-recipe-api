"""
This module is a blueprint for cli commands.
"""

# Import statements
from datetime import date
from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.category import Category
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.instruction import Instruction
# from models.saved_recipe import SavedRecipe

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def db_create():
    """
    Custom Flask CLI command to drop and recreate database tables and populate initial data.

    Drops all existing tables, creates new ones based on SQLAlchemy models,
    and adds initial data for users, categories, recipes, ingredients, and instructions.
    """

    # Drop all existing tables
    db.drop_all()

    # Create all tables based on SQLAlchemy models
    db.create_all()

    # Print message confirming table creation
    print('Created tables')

    # Define initial data lists for users, categories, recipes, ingredients, and instructions
    users = [
        # username & email are unique for each user
        # use bcrypt for slow hashing of password
        User(
            email='admin@example.com',
            password=bcrypt.generate_password_hash('hashed_password1').decode('utf-8'),
            name='admin',
            is_admin=True
        ),
        User(
            email='user@example.com',
            password=bcrypt.generate_password_hash('hashed_password2').decode('utf-8'),
            name='John1'
        )
    ]

    categories = [
        Category(name='Italian'),
        Category(name='Mexican')
    ]

    recipes = [
        # description & preparation_time are optional
        # is_public default value is True
        Recipe(title='Spaghetti Carbonara', description='A classic Italian pasta dish.', date_created=date.today(), preparation_time=30),
        Recipe(title='Tacos', date_created=date.today(), is_public=False)
    ]

    ingredients = [
        # quantity is optional
        Ingredient(name='Spaghetti', quantity='200g'),
        Ingredient(name='Eggs', quantity='4'),
        Ingredient(name='Bacon', quantity='100g'),
        Ingredient(name='Tortillas'),
        Ingredient(name='Chicken', quantity='200g')
    ]

    instructions = [
        Instruction(description='Boil the spaghetti.', order=1),
        Instruction(description='Fry the bacon.', order=2),
        Instruction(description='Mix eggs with cheese.', order=3),
        Instruction(description='Cook the chicken.', order=1),
        Instruction(description='Assemble the tacos.', order=2)
    ]

    # Add initial data to the session
    db.session.add_all(users)
    db.session.add_all(categories)
    db.session.add_all(recipes)
    db.session.add_all(ingredients)
    db.session.add_all(instructions)

    # Commit the session to persist changes to the database
    db.session.commit()

    # saved_recipes = [
    #     SavedRecipe(user_id=user1.id, recipe_id=recipe1.id, notes='Try this with extra cheese.'),
    #     SavedRecipe(user_id=user2.id, recipe_id=recipe2.id, notes='Add more spice for a kick.')
    # ]

    # db.session.add_all(saved_recipes)
    # db.session.commit()
