"""
This module is a blueprint for routes to manage category records.
"""

from flask import Blueprint
from init import db
from models.category import Category, CategorySchema

# Define the Blueprint for category routes
categories_bp = Blueprint('categories', __name__, url_prefix='/categories')

@categories_bp.route("/")
def all_categories():
    """
    Route to fetch all categories from the database.

    Returns:
        list: A JSON representation of all category records.
    """
    # Construct a SQL statement to select all categories
    stmt = db.select(Category)
    # Execute the statement and fetch all categories
    categories = db.session.scalars(stmt).all()
    # Serialize the categories to JSON format using CategorySchema
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

    # Serialize the category record to JSON format
    return CategorySchema().dump(category)