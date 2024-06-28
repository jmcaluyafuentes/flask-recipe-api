"""
This module defines Flask CLI commands for database management.
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

# Define a Blueprint for CLI commands
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
        User(
            email='admin@example.com',
            password=bcrypt.generate_password_hash('password_admin').decode('utf-8'),
            name='admin',
            is_admin=True
        ),
        User(
            email='user1@example.com',
            password=bcrypt.generate_password_hash('password_user1').decode('utf-8'),
            name='John'
        )
    ]

    categories = [
        Category(
            cuisine_name='Italian'
        ),
        Category(
            cuisine_name='Mexican'
        )
    ]

    # Add initial data to the session
    db.session.add_all(users)
    db.session.add_all(categories)

    # Commit the session to persist changes to the database
    db.session.commit()

    recipes = [
        Recipe(
            title='Spaghetti Carbonara',
            description='A classic Italian pasta dish.',
            date_created=date.today(),
            preparation_time=30,
            user=users[0],
            category=categories[0],
        ),
        Recipe(
            title='Tacos',
            date_created=date.today(),
            is_public=False,
            user=users[1],
            category=categories[1],
        )
    ]

    # Add initial data to the session
    db.session.add_all(recipes)

    # Commit the session to persist changes to the database
    db.session.commit()

    ingredients = [
        # Ingredients of the first recipe
        Ingredient(
            name='Spaghetti',
            quantity='200g',
            recipe=recipes[0]
        ),
        Ingredient(
            name='Eggs',
            quantity='4',
            recipe=recipes[0]
        ),
        Ingredient(
            name='Bacon',
            quantity='100g',
            recipe=recipes[0],
        ),

        # Ingredients of the second recipe
        Ingredient(
            name='Tortillas',
            recipe=recipes[1]
        ),
        Ingredient(
            name='Chicken',
            quantity='200g',
            recipe=recipes[1]
        )
    ]

    instructions = [
        # Instructions of the first recipe
        Instruction(
            step_number=1,
            task='Boil the spaghetti.',
            recipe=recipes[0]
        ),
        Instruction(
            step_number=2,
            task='Fry the bacon.',
            recipe=recipes[0]
        ),
        Instruction(
            step_number=3,
            task='Mix eggs with cheese.',
            recipe=recipes[0]
        ),

        # Instructions of the first recipe
        Instruction(
            step_number=1,
            task='Cook the chicken.',
            recipe=recipes[1]
        ),
        Instruction(
            step_number=2,
            task='Assemble the tacos.',
            recipe=recipes[1]
        )
    ]

    # Add initial data to the session
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
