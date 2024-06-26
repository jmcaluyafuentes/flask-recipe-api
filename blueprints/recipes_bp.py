"""
This module is a blueprint for routes to manage recipe records.
"""

from datetime import date
import random
from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
from init import db
from models.recipe import Recipe, RecipeSchema
from models.ingredient import Ingredient
from models.instruction import Instruction
from models.category import Category
from models.user import User
from auth import authorize_owner, current_user_is_admin

# Define a blueprint for recipe-related routes
recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route("/public")
def all_public_recipes():
    """
    Route to fetch all public recipes from the database.

    Returns:
        list of dict: A JSON representation of all user records.
    """
    # Query all recipes where is_public is True
    recipes = Recipe.query.filter_by(is_public=True).all()

    # Return the serialized recipes
    return RecipeSchema(many=True).dump(recipes)

@recipes_bp.route("/all")
@jwt_required()  # Ensure only authenticated users can access this route
def get_all_recipes():
    """
    Retrieve all recipes (both public and private) from the database. Only the admin can access this resource.

    Returns:
        list of dict: A JSON representation of all recipes.
    """
    # Check if the current user is an admin
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if not current_user.is_admin:
        return {"message": "Unauthorized, admin access required"}, 403

    # Fetch all recipes from the database
    all_recipes = Recipe.query.all()

    # Return the serialized recipes
    return RecipeSchema(many=True).dump(all_recipes)

@recipes_bp.route("/<int:recipe_id>")
@jwt_required()
def one_recipe(recipe_id):
    """
    Retrieve a recipe record by its ID. Only accessible to admin or the user who created the recipe.

    Args:
        recipe_id (int): The ID of the recipe to retrieve.

    Returns:
        dict: A JSON representation of the recipe record.
    """
    # Get the current user's ID from the JWT payload
    current_user_id = get_jwt_identity()

    # Fetch the recipe with the specified ID, or return a 404 error if not found
    recipe = db.get_or_404(Recipe, recipe_id)

    # Check if the current user is either an admin or the author of the recipe
    if current_user_id != recipe.user_id and not current_user_is_admin():
        return {"error": "You are not authorized to access this resource"}, 403

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

@recipes_bp.route('/public/filter')
def filter_recipes():
    """
    Endpoint to filter public recipes based on title, preparation time, ingredient name, and cuisine name.

    Query Parameters:
        - title: Title or name of the recipe (string)
        - prep_time: Exact preparation time in minutes (integer)
        - ingredient_name: Name of the ingredient (string)
        - cuisine_name: Name of the cuisine category (string)

    Returns:
        list: A JSON representation of filtered recipes or an error if no match is found for any parameter.
    """
    # Define valid parameters
    valid_params = {'title', 'prep_time', 'ingredient_name', 'cuisine_name'}
    
    # Retrieve query parameters
    query_params = request.args.to_dict()
    
    # Check for invalid parameters
    invalid_params = [param for param in query_params if param not in valid_params]
    if invalid_params:
        return {"error": f"Invalid parameter(s): {', '.join(invalid_params)}"}, 400

    # Extract valid query parameters
    title = query_params.get('title')
    prep_time = query_params.get('prep_time')
    ingredient_name = query_params.get('ingredient_name')
    cuisine_name = query_params.get('cuisine_name')

    # Base query for public recipes
    query = Recipe.query.filter_by(is_public=True)

    # Apply filters based on valid query parameters
    if title:
        query = query.filter(Recipe.title.ilike(f"%{title}%"))
    if prep_time:
        try:
            prep_time = int(prep_time)
            query = query.filter(Recipe.preparation_time == prep_time)
        except ValueError:
            return {"error": "Invalid preparation time. Must be a valid integer."}, 400
    if ingredient_name:
        query = query.join(Recipe.ingredients).filter(Ingredient.name.ilike(f"%{ingredient_name}%"))
    if cuisine_name:
        query = query.join(Recipe.category).filter(Category.cuisine_name.ilike(f"%{cuisine_name}%"))

    # Execute the query to fetch filtered recipes
    filtered_recipes = query.all()

    # Check if any recipes were found
    if not filtered_recipes:
        return {"error": "No recipes found matching the specified criteria."}, 404

    # Serialize the filtered recipes
    return RecipeSchema(many=True).dump(filtered_recipes)

@recipes_bp.route('/user/<int:user_id>/category/<int:category_id>')
@jwt_required()
def recipes_by_user_and_category(user_id, category_id):
    """
    Retrieve recipes by the user who created them filtered by category.

    Args:
        category_id (int): The ID of the category to fetch recipes for.
        user_id (int): The ID of the user who created the recipes.

    Returns:
        list of dict: A JSON representation of recipes matching the criteria.
    """
    # Get the current user ID from the JWT payload
    current_user_id = get_jwt_identity()

    # Ensure the current user is requesting their own recipes or they are an admin
    if current_user_id != user_id and not current_user_is_admin():
        return {"error": "Unauthorized access"}, 403

    # Query the database to fetch the category by its ID
    category = db.session.query(Category).get(category_id)

    if not category:
        return {"error": "Category not found"}, 404

    # Retrieve recipes by category and user ID
    recipes = Recipe.query.filter_by(category_id=category_id, user_id=user_id).all()

    # Serialize the recipe record to JSON format
    return RecipeSchema(many=True).dump(recipes)

@recipes_bp.route('/user/random')
@jwt_required()
def recipes_by_user_and_random():
    """
    Endpoint to fetch a randomly selected recipe from both private recipes created by the user and the public recipes.

    Returns:
        dict: A JSON representation of the randomly selected recipe.
    """
    current_user_id = get_jwt_identity()

    # Query private recipes of the current user
    private_recipes = Recipe.query.filter_by(user_id=current_user_id).all()

    # Query public recipes
    public_recipes = Recipe.query.filter_by(is_public=True).all()

    # Combine private and public recipes
    all_recipes = private_recipes + public_recipes

    if not all_recipes:
        abort(404, description="No recipes found.")

    # Select a random recipe from all_recipes
    random_recipe_by_user = random.choice(all_recipes)

    # Serialize the selected recipe
    return RecipeSchema().dump(random_recipe_by_user)

@recipes_bp.route("/public/random")
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

@recipes_bp.route("/<int:recipe_id>", methods=["DELETE"])
@jwt_required()
def delete_recipe(recipe_id):
    """
    Endpoint to delete an existing recipe. Accessible by admin or the user who created the recipe.

    Args:
        recipe_id (int): The ID of the recipe to be deleted.

    Returns:
        dict: A JSON response indicating the outcome of the deletion.
            - {}: A response indicating that the recipe was successfully deleted.
            - int: HTTP status code 200 indicating success.
            - int: HTTP status code 403 if the user is not authorized.
            - int: HTTP status code 404 if the recipe does not exist.
            - int: HTTP status code 500 if an error occurred while deleting the recipe.
    """
    try:
        # Fetch the recipe with the specified ID, or raise a NoResultFound exception if not found
        recipe = Recipe.query.filter_by(recipe_id=recipe_id).one()

        # Get the ID of the current user from the JWT
        current_user_id = get_jwt_identity()

        # Check if the current user is the author of the recipe or an admin
        if current_user_id != recipe.user_id and not current_user_is_admin():
            return {"error": "You are not authorized to delete this recipe."}, 403

        # Delete the recipe from the database
        db.session.delete(recipe)
        db.session.commit()

        # Return an empty dictionary to signify successful deletion
        return {}, 200

    except NoResultFound:
        # Handle case where the recipe with the specified ID does not exist
        return {"error": "Recipe not found."}, 404

    except SQLAlchemyError:
        # Rollback the session to undo any partial changes due to a general SQLAlchemy error
        db.session.rollback()
        # Return a generic error message indicating a database error with a 500 Internal Server Error status code
        return {"error": "An error occurred while deleting the recipe."}, 500

