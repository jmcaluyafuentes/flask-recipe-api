"""
This module is a blueprint for routes to manage recipe records.
"""

from datetime import date
import random
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from init import db
from models.recipe import Recipe, RecipeSchema

# Define a blueprint for recipe-related routes
recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route("/")
def all_recipes():
    """
    Route to fetch all recipes from the database.

    :return: A JSON representation of all recipe records.
    :return_type: list of dict
    """
    # Create a select statement to fetch all recipes
    stmt = db.select(Recipe)
    # Execute the query and fetch all recipes
    recipes = db.session.scalars(stmt).all()
    # Return the serialized recipes
    return RecipeSchema(many=True).dump(recipes)

@recipes_bp.route("/<int:recipe_id>")
def one_recipe(recipe_id):
    """
    Retrieve a recipe record by its ID.

    :param id: The ID of the recipe to retrieve.
    :type recipe_id: int
    :return: A JSON representation of the recipe record.
    :r_type: dict
    """
    # Fetch the recipe with the specified ID, or return a 404 error if not found
    recipe = db.get_or_404(Recipe, recipe_id)
    # Serialize the recipe record to JSON format
    return RecipeSchema().dump(recipe)

@recipes_bp.route("/", methods=["POST"])
@jwt_required()
def create_recipe():
    """
    This function handles POST requests to create a new recipe. It expects the request 
    body to contain the recipe's title, description, is_public flag, and preparation time. 
    The description is optional and defaults to an empty string if not provided. 
    The is_public flag defaults to True, and the preparation time is optional.

    Request Body (JSON):
    title (str): The title of the recipe.
    description (str, optional): The description of the recipe.
    is_public (bool, optional): The visibility status of the recipe.
    preparation_time (int, optional): The preparation time in minutes.

    Returns:
        tuple: A tuple containing the serialized recipe data and an HTTP status code.
            - dict: The serialized recipe data.
            - int: HTTP status code 201 indicating that the recipe was successfully created.

    Raises:
        ValidationError: If the input data does not conform to the expected schema.
        KeyError: If there is a missing field.
    """
    # Load the request data and validate it against the RecipeSchema
    recipe_info = RecipeSchema(only=['title', 'description', 'is_public', 'preparation_time']).load(request.json, unknown='exclude')

    # Create a new Recipe instance
    recipe = Recipe (
        title=recipe_info['title'],
        description=recipe_info.get('description', ''),
        is_public=recipe_info.get('is_public', True),
        preparation_time=recipe_info.get('preparation_time', None),
        date_created=date.today()
    )

    # Add the new recipe to the session and commit it to the database
    db.session.add(recipe)
    db.session.commit()
    # Return the serialized recipe data and a 201 Created status code
    return RecipeSchema().dump(recipe), 201

@recipes_bp.route("/<int:recipe_id>", methods=["PUT", "PATCH"])
def update_recipe(recipe_id):
    """
    This function handles PUT and PATCH requests to update an existing recipe by its ID. 
    It expects the request body to contain one or more fields of the recipe that need to be updated, 
    including title, description, is_public flag, and preparation time. Any fields not provided 
    in the request will remain unchanged.

    Path Parameters:
        recipe_id (int): The ID of the recipe to be updated.

    Request Body (JSON):
        title (str, optional): The new title of the recipe.
        description (str, optional): The new description of the recipe.
        is_public (bool, optional): The new visibility status of the recipe.
        preparation_time (int, optional): The new preparation time in minutes.

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
    # Load the request data and validate it against the RecipeSchema
    recipe_info = RecipeSchema(only=['title', 'description', 'is_public', 'preparation_time']).load(request.json, unknown='exclude')

    # Update the recipe fields if new values are provided, otherwise keep the existing values
    recipe.title = recipe_info.get('title', recipe.title)
    recipe.description = recipe_info.get('description', recipe.description)
    recipe.is_public = recipe_info.get('is_public', recipe.is_public)
    recipe.preparation_time = recipe_info.get('preparation_time', recipe.preparation_time)
    # Commit the changes to the database
    db.session.commit()
    # Return the serialized updated recipe data and a 200 OK status code
    return RecipeSchema().dump(recipe)

@recipes_bp.route("/<recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    """
    This endpoint handles DELETE requests to remove a recipe from the database 
    based on its unique identifier (ID). If the recipe with the specified ID exists, 
    it is deleted from the database. If not found, a 404 error is returned.

    Path Parameters:
        recipe_id (int): The ID of the recipe to be deleted.

    Returns:
        dict: An empty dictionary indicating successful deletion with 200 status code.

    Raises:
        NotFound: If the recipe with the given ID does not exist in the database.
    """
    # Fetch the recipe with the specified ID, or return a 404 error if not found
    recipe = db.get_or_404(Recipe, recipe_id)

    # Delete the recipe from the database
    db.session.delete(recipe)
    db.session.commit()

    # Return an empty dictionary to signify successful deletion with 200 status code.
    return {}

@recipes_bp.route("/random", methods=["GET"])
def random_recipe():
    """
    Retrieve a random recipe from the database.

    Returns:
        dict: A JSON representation of a random recipe record.
    """
    # Fetch all recipe IDs from the database
    all_recipe_ids = [recipe.id for recipe in Recipe.query.all()]

    if not all_recipe_ids:
        # Handle case where there are no recipes in the database
        return {"message": "No recipes found"}, 404

    # Choose a random recipe ID
    random_recipe_id = random.choice(all_recipe_ids)

    # Fetch the recipe with the random ID
    recipe = Recipe.query.get(random_recipe_id)

    # Serialize the recipe record to JSON format
    return RecipeSchema().dump(recipe)
