"""RecipeRoutes"""
from flask_jwt_extended import jwt_required
from flask import Blueprint
from api.controllers.RecipeController import RecipeController
from api.services.RecipeService import RecipeService
from api.database.RecipeDatabase import RecipeDatabase
from api.externalServices.Authentication import Authentication

recipe_blueprint = Blueprint('recipe', __name__)

recipe_database = RecipeDatabase()
recipe_service = RecipeService(recipe_database, Authentication)
recipe_controller = RecipeController(recipe_service)

@recipe_blueprint.route("/create-recipe", methods=["POST"])
@jwt_required()
def create_recipe():
    """Endpoint that receives ingredients and returns a recipe"""
    return recipe_controller.create_recipe()

@recipe_blueprint.route("/get-recipes", methods=["GET"])
@jwt_required()
def get_recipes():
    """Endpoint that receives a token and returns the recipes from the user"""
    return recipe_controller.get_recipes()

@recipe_blueprint.route("/get-recipe/<string:recipe_id>", methods=["GET"])
@jwt_required()
def get_recipe_by_id(recipe_id):
    """Endpoint that receives a token and a recipe_id and returns the recipe from the user"""
    return recipe_controller.get_recipe_by_id(recipe_id)