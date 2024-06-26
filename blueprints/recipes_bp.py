"""
This module is a blueprint for routes to manage recipe records.
"""

from datetime import date
from flask import Blueprint, request
from init import db
from models.recipe import Recipe, RecipeSchema

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route("/")
def all_recipes():
    """
    Route to fetch all recipes from the database.

    :return: A JSON representation of all recipe records.
    :return_type: list of dict
    """
    stmt = db.select(Recipe)
    recipes = db.session.scalars(stmt).all()
    return RecipeSchema(many=True).dump(recipes)

@recipes_bp.route("/<int:recipe_id>")
def one_recipe(recipe_id):
    """
    Retrieve a recipe record by its ID.

    :param id: The ID of the recipe to retrieve.
    :type id: int
    :return: A JSON representation of the recipe record.
    :return_type: dict
    """
    # Fetch the recipe with the specified ID, or return a 404 error if not found
    recipe = db.get_or_404(Recipe, recipe_id)

    # Serialize the recipe record to JSON format
    return RecipeSchema().dump(recipe)

@recipes_bp.route("/", methods=["POST"])
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
        KeyError: If the input data does not conform to the expected schema.
    """

    recipe_info = RecipeSchema(only=['title', 'description', 'is_public', 'preparation_time']).load(request.json, unknown='exclude')

    recipe = Recipe (
        title=recipe_info['title'],
        description=recipe_info.get('description', ''),
        is_public=recipe_info.get('is_public', True),
        preparation_time=recipe_info.get('preparation_time', None),
        date_created=date.today()
    )

    db.session.add(recipe)
    db.session.commit()
    return RecipeSchema().dump(recipe)
