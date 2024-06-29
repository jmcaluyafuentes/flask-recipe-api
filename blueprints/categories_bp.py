"""
This module is a blueprint for routes to manage category records.
"""

from flask import Blueprint
from init import db
from models.category import Category, CategorySchema

# Define a blueprint for category-related routes
categories_bp = Blueprint('categories', __name__, url_prefix='/categories')

@categories_bp.route("/")
def all_categories():
    """
    Route to fetch all categories from the database.

    Returns:
        list: A JSON representation of all category records.
    """
    # Query the database for all category records
    categories = Category.query.all()

    # Check if categories are found
    if not categories:
        return {"error": "No categories found."}, 404

    # Return the serialized categories
    return CategorySchema(many=True).dump(categories)

@categories_bp.route("/<int:category_id>")
def one_category(category_id):
    """
    Retrieve a category record by its ID.

    Args:
        category_id (int): The ID of the category to retrieve.

    Returns:
        dict: A JSON representation of the category record.
    """
    # Fetch the category with the specified ID, or return a 404 error if not found
    category = db.get_or_404(Category, category_id)

    # Return the serialized category
    return CategorySchema().dump(category)
