"""
This module is a blueprint for routes to manage recipe records.
"""

from datetime import date
import random
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from init import db
from models.recipe import Recipe, RecipeSchema
from models.ingredient import Ingredient
from models.instruction import Instruction
from models.category import Category
from auth import authorize_owner

# Define a blueprint for recipe-related routes
recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route("/")
def all_recipes():
    """
    Route to fetch all public recipes from the database.

    Returns:
        list of dict: A JSON representation of all user records.
    """
    # Query all recipes where is_public is True
    recipes = Recipe.query.filter_by(is_public=True).all()

    # Return the serialized recipes
    return RecipeSchema(many=True).dump(recipes)

@recipes_bp.route("/<int:recipe_id>")
def one_recipe(recipe_id):
    """
    Retrieve a recipe record by its ID.

    Args:
        recipe_id (int): The ID of the recipe to retrieve.

    Returns:
        dict: A JSON representation of the recipe record.
    """
    # Fetch the recipe with the specified ID, or return a 404 error if not found
    recipe = db.get_or_404(Recipe, recipe_id)

    # Return the serialized recipe
    return RecipeSchema().dump(recipe)

@recipes_bp.route("/user")
@jwt_required()
def get_user_recipes():
    """
    Route to fetch all recipes associated with the authenticated user.

    Returns:
        list of dict: A JSON representation of all recipes associated with the user.
    """
    # Get the ID of the authenticated user
    current_user_id = get_jwt_identity()

    # Query all recipes associated with the current user
    recipes = Recipe.query.filter_by(user_id=current_user_id).all()

    # Return the serialized recipe
    return RecipeSchema(many=True).dump(recipes), 200

@recipes_bp.route("/", methods=["POST"])
@jwt_required()
def create_recipe():
    """
    This function handles POST requests to create a new recipe. It expects the request 
    body to contain the recipe's title, description, is_public flag, and preparation time. 
    The description is optional and defaults to an empty string if not provided. 
    The is_public flag defaults to True, and the preparation time is optional.

    Returns:
        tuple: A tuple containing the serialized recipe data and an HTTP status code.
            - dict: The serialized recipe data.
            - int: HTTP status code 201 indicating that the recipe was successfully created.

    Raises:
        ValidationError: If the input data does not conform to the expected schema.
        KeyError: If there is a missing field.
    """
    try:
        # Load the request data and validate it against the RecipeSchema
        recipe_info = RecipeSchema(only=['title', 'description', 'is_public', 'preparation_time', 'category', 'ingredients', 'instructions']).load(request.json, unknown='exclude')
        
        # Extract category information from the request
        category_data = recipe_info.get('category', {})
        cuisine_name = category_data.get('cuisine_name') if isinstance(category_data, dict) else None

        # Extract ingredients information from the request
        ingredients_data = recipe_info.get('ingredients', [])

        # Extract instructions information from the request
        instructions_data = recipe_info.get('instructions', [])

        # Initialize category variable to None
        category = None

        # If cuisine_name is provided, find or create the corresponding category
        if cuisine_name:
            category = Category.query.filter_by(cuisine_name=cuisine_name).first()
            if not category:
                category = Category(cuisine_name=cuisine_name)
                db.session.add(category)
                db.session.commit()

        # Create a new Recipe instance
        recipe = Recipe (
            title=recipe_info['title'],
            description=recipe_info.get('description', ''),
            is_public=recipe_info.get('is_public', True),
            preparation_time=recipe_info.get('preparation_time', None),
            date_created=date.today(),
            user_id=get_jwt_identity(),
            category=category  # Assign the category instance if it exists or None
        )

        # Add the new recipe to the session and commit it to the database
        db.session.add(recipe)
        db.session.commit()

        # Create and add ingredients to the recipe
        ingredients = []
        for ingredient_data in ingredients_data:
            ingredient = Ingredient(
                name=ingredient_data['name'],
                quantity=ingredient_data.get('quantity'),
                recipe=recipe
            )
            db.session.add(ingredient)
            ingredients.append(ingredient)
        db.session.commit()

        # Create and add instructions to the recipe
        instructions = []
        for instruction_data in instructions_data:
            instruction = Instruction(
                step_number=instruction_data['step_number'],
                task=instruction_data['task'],
                recipe=recipe
            )
            db.session.add(instruction)
            instructions.append(instruction)
        db.session.commit()

        # Return the serialized recipe data and a 201 Created status code
        return RecipeSchema().dump(recipe), 201

    except IntegrityError as _:
        # Rollback the session to undo any partial changes due to an integrity constraint violation
        db.session.rollback()
        # Return an error message indicating that the recipe title already exists with a 400 Bad Request status code
        return {"error": "Recipe title already exists. Please choose a different title."}, 400

    except SQLAlchemyError as _:
        # Rollback the session to undo any partial changes due to a general SQLAlchemy error
        db.session.rollback()
        # Return a generic error message indicating a database error with a 500 Internal Server Error status code
        return {"error": "An error occurred while creating the recipe."}, 500

@recipes_bp.route("/<int:recipe_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_recipe(recipe_id):
    """
    Endpoint to update an existing recipe.

    This function handles PUT and PATCH requests to update an existing recipe by its ID. 
    It expects the request body to contain one or more fields of the recipe that need to be updated, 
    including title, description, is_public flag, and preparation time. Any fields not provided 
    in the request will remain unchanged.

    Args:
        recipe_id (int): The ID of the user to be updated.

    Returns:
        tuple: A tuple containing the serialized updated recipe data and an HTTP status code.
            - dict: The serialized updated recipe data.
            - int: HTTP status code 200 indicating that the recipe was successfully updated.

    Raises:
        ValidationError: If the input data does not conform to the expected schema.
        NotFound: If the recipe with the given ID does not exist.
    """
    # Fetch the recipe with the specified ID, or return a 404 error if not found
    recipe = db.get_or_404(Recipe, recipe_id)

    # Call the function that check if the JWT user is the author of the given recipe
    authorize_owner(recipe)

    # Load the request data and validate it against the RecipeSchema
    recipe_info = RecipeSchema(only=['title', 'description', 'is_public', 'preparation_time', 'category', 'ingredients', 'instructions']).load(request.json, unknown='exclude')

    # Update the recipe fields if new values are provided, otherwise keep the existing values
    recipe.title = recipe_info.get('title', recipe.title)
    recipe.description = recipe_info.get('description', recipe.description)
    recipe.is_public = recipe_info.get('is_public', recipe.is_public)
    recipe.preparation_time = recipe_info.get('preparation_time', recipe.preparation_time)

    # Update the category if provided
    if 'category' in recipe_info:
        category_data = recipe_info['category']
        cuisine_name = category_data.get('cuisine_name')
        if cuisine_name:
            category = Category.query.filter_by(cuisine_name=cuisine_name).first()
            if not category:
                category = Category(cuisine_name=cuisine_name)
                db.session.add(category)
                db.session.commit()
            recipe.category = category

    # Update or add ingredients if provided
    if 'ingredients' in recipe_info:
        new_ingredient_data = recipe_info['ingredients']

        # Get current ingredients as a dictionary for easy lookup by ID
        current_ingredients = {ing.ingredient_id: ing for ing in recipe.ingredients}

        for ingredient_data in new_ingredient_data:
            ingredient_id = ingredient_data.get('id')

            if ingredient_id and ingredient_id in current_ingredients:
                # Update existing ingredient
                ingredient = current_ingredients[ingredient_id]
                ingredient.name = ingredient_data.get('name', ingredient.name)
                ingredient.quantity = ingredient_data.get('quantity', ingredient.quantity)
            else:
                # Add new ingredient
                new_ingredient = Ingredient(
                    name=ingredient_data['name'],
                    quantity=ingredient_data.get('quantity'),
                    recipe_id=recipe.recipe_id  # Ensure recipe_id is set for new ingredients
                )
                db.session.add(new_ingredient)

        # Remove ingredients that are not in the new data
        new_ingredient_ids = {ing.get('id') for ing in new_ingredient_data if ing.get('id')}
        for ingredient_id in list(current_ingredients.keys()):
            if ingredient_id not in new_ingredient_ids:
                db.session.delete(current_ingredients[ingredient_id])

    # Update or add instructions if provided
    if 'instructions' in recipe_info:
        new_instruction_data = recipe_info['instructions']

        # Get current instructions as a dictionary for easy lookup by ID
        current_instructions = {instr.instruction_id: instr for instr in recipe.instructions}

        for instruction_data in new_instruction_data:
            instruction_id = instruction_data.get('id')

            if instruction_id and instruction_id in current_instructions:
                # Update existing instruction
                instruction = current_instructions[instruction_id]
                instruction.step_number = instruction_data.get('step_number', instruction.step_number)
                instruction.task = instruction_data.get('task', instruction.task)
            else:
                # Add new instruction
                new_instruction = Instruction(
                    step_number=instruction_data['step_number'],
                    task=instruction_data['task'],
                    recipe_id=recipe.recipe_id  # Ensure recipe_id is set for new instructions
                )
                db.session.add(new_instruction)

        # Remove instructions that are not in the new data
        new_instruction_ids = {instr.get('id') for instr in new_instruction_data if instr.get('id')}
        for instruction_id in list(current_instructions.keys()):
            if instruction_id not in new_instruction_ids:
                db.session.delete(current_instructions[instruction_id])

    # Commit the updated recipe to the database
    db.session.commit()

    # Return the serialized updated recipe data
    return RecipeSchema().dump(recipe)

@recipes_bp.route("/<recipe_id>", methods=["DELETE"])
@jwt_required()
def delete_recipe(recipe_id):
    """
    This endpoint handles DELETE requests to remove a recipe from the database 
    based on its unique identifier (ID). If the recipe with the specified ID exists, 
    it is deleted from the database. If not found, a 404 error is returned.

    Args:
        recipe_id (int): The ID of the recipe to be updated.

    Returns:
        dict: An empty dictionary indicating successful deletion with 200 status code.

    Raises:
        NotFound: If the recipe with the given ID does not exist in the database.
    """
    # Fetch the recipe with the specified ID, or return a 404 error if not found
    recipe = db.get_or_404(Recipe, recipe_id)

    # Call the function that check if the JWT user is the author of the given recipe
    authorize_owner(recipe)

    # Delete the recipe from the database
    db.session.delete(recipe)
    db.session.commit()

    # Return an empty dictionary to signify successful deletion.
    return {}

@recipes_bp.route("/random")
def random_recipe():
    """
    Retrieve a random public recipe from the database.

    Returns:
        dict: A JSON representation of a random public recipe record.
    """
    # Fetch all public recipe IDs from the database
    public_recipe_ids = [recipe.recipe_id for recipe in Recipe.query.filter_by(is_public=True).all()]

    if not public_recipe_ids:
        # Handle case where there are no public recipes in the database
        return {"message": "No public recipes found"}, 404

    # Choose a random public recipe ID
    random_recipe_id = random.choice(public_recipe_ids)

    # Fetch the recipe with the random public ID
    recipe = Recipe.query.get(random_recipe_id)

    # Serialize the recipe record to JSON format
    return RecipeSchema().dump(recipe)
