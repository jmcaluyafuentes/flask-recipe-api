"""
This module is a blueprint for routes to manage category records.
"""

from flask import Blueprint
from init import db
from models.category import Category, CategorySchema

categories_bp = Blueprint('categories', __name__, url_prefix='/categories')

@categories_bp.route("/")
def all_categories():
    """
    Route to fetch all categories from the database.

    :return: A JSON representation of all category records.
    :return_type: list of dict
    """
    stmt = db.select(Category)
    categories = db.session.scalars(stmt).all()
    return CategorySchema(many=True).dump(categories)

@categories_bp.route("/<int:cat_id>")
def one_category(cat_id):
    """
    Retrieve a category record by its ID.

    :param id: The ID of the category to retrieve.
    :type id: int
    :return: A JSON representation of the category record.
    :return_type: dict
    """
    # Fetch the category with the specified ID, or return a 404 error if not found
    category = db.get_or_404(Category, cat_id)

    # Serialize the category record to JSON format
    return CategorySchema().dump(category)