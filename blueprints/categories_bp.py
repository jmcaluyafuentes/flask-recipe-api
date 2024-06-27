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
    stmt = db.select(Category)
    # Execute the query and fetch all categories
    categories = db.session.scalars(stmt).all()

    # Return the serialized categories
    return CategorySchema(many=True).dump(categories)

@categories_bp.route("/<int:cat_id>")
def one_category(cat_id):
    """
    Retrieve a category record by its ID.

    Args:
        cat_id (int): The ID of the category to retrieve.

    Returns:
        dict: A JSON representation of the category record.
    """
    # Fetch the category with the specified ID, or return a 404 error if not found
    category = db.get_or_404(Category, cat_id)

    # Return the serialized category
    return CategorySchema().dump(category)