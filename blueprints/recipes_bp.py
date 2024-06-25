"""
This module is a blueprint for routes to manage recipe records.
"""

from flask import Blueprint
from init import db
from models.recipe import Recipe, RecipeSchema

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

# Route to get all records
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

# Route to get a record based on id
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
