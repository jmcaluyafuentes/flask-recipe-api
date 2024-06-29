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
            email='user_1_@example.com',
            password=bcrypt.generate_password_hash('password_user1').decode('utf-8'),
            name='User_1'
        ),
        User(
            email='user_2_@example.com',
            password=bcrypt.generate_password_hash('password_user2').decode('utf-8'),
            name='User_2'
        )
    ]

    categories = [
        Category(
            cuisine_name='Italian'
        ),
        Category(
            cuisine_name='Mexican'
        ),
        Category(
            cuisine_name='Filipino'
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
        ),
        Recipe(
            title='Chiles Rellenos',
            description='Roasted poblano peppers stuffed with cheese',
            date_created=date.today(),
            user=users[1],
            category=categories[1],
        ),
        Recipe(
            title='Menudo',
            description= 'A hearty stew made with pork.',
            date_created=date.today(),
            user=users[2],
            category=categories[2],
        ),
        Recipe(
            title='Arroz Caldo',
            description= 'Rice porridge flavored with ginger and garlic.',
            date_created=date.today(),
            user=users[2],
            category=categories[2],
        )
    ]

    # Add initial data to the session
    db.session.add_all(recipes)

    # Commit the session to persist changes to the database
    db.session.commit()

    ingredients = [
        # Ingredients of the 1st recipe
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

        # Ingredients of the 2nd recipe
        Ingredient(
            name='Tortillas',
            recipe=recipes[1]
        ),
        Ingredient(
            name='Chicken',
            quantity='200g',
            recipe=recipes[1]
        ),

        # Ingredients of the 3rd recipe
        Ingredient(
            name='Peppers',
            quantity='6',
            recipe=recipes[2]
        ),
        Ingredient(
            name='Cheese',
            quantity='1 1/2',
            recipe=recipes[2]
        ),

        # Ingredients of the 4th recipe
        Ingredient(
            name='Pork',
            quantity='1 kg',
            recipe=recipes[3]
        ),
        Ingredient(
            name='Potatoes',
            quantity='2',
            recipe=recipes[3]
        ),

        # Ingredients of the 5th recipe
        Ingredient(
            name='Glutinous rice',
            quantity='1 cup',
            recipe=recipes[4]
        ),
        Ingredient(
            name='Chicken',
            quantity='1/2 kilo',
            recipe=recipes[4]
        )
    ]

    instructions = [
        # Instructions of the 1st recipe
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

        # Instructions of the 2nd recipe
        Instruction(
            step_number=1,
            task='Cook the chicken.',
            recipe=recipes[1]
        ),
        Instruction(
            step_number=2,
            task='Assemble the tacos.',
            recipe=recipes[1]
        ),

        # Instructions of the 3rd recipe
        Instruction(
            step_number=1,
            task='Roast the Peppers.',
            recipe=recipes[2]
        ),
        Instruction(
            step_number=2,
            task='Make the Tomato Sauce.',
            recipe=recipes[2]
        ),

        # Instructions of the 4th recipe
        Instruction(
            step_number=1,
            task='Marinate the Pork.',
            recipe=recipes[3]
        ),
        Instruction(
            step_number=2,
            task='Cook the Pork.',
            recipe=recipes[3]
        ),

        # Instructions of the 5th recipe
        Instruction(
            step_number=1,
            task='Sauté Aromatics.',
            recipe=recipes[4]
        ),
        Instruction(
            step_number=2,
            task='Cook the Chicken.',
            recipe=recipes[4]
        )
    ]

    # Add initial data to the session
    db.session.add_all(ingredients)
    db.session.add_all(instructions)

    # Commit the session to persist changes to the database
    db.session.commit()
