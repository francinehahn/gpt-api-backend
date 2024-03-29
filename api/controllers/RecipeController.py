"""Recipe controller"""
from marshmallow import ValidationError
from flask import jsonify, request
from botocore.exceptions import ClientError
from api.errors.RecipeErrors import RecipeNotFound
from api.errors.RecipeErrors import NoRecipesToUpdate

class RecipeController:
    """This class receives data from the HTTP request and returns the response"""
    def __init__(self, recipe_service):
        self.recipe_service = recipe_service

    def create_recipe(self):
        """This method receives ingredients and returns a recipe"""
        try:
            data = request.json
            response = self.recipe_service.create_recipe(data)
            response = jsonify(
                message = "The recipe has been registered successfully",
                data = response
            )
            response.status_code = 201
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except ValidationError as err:
            response = jsonify(
                error = f"Validation error: {err}"
            )
            response.status_code = 422
            return response
        except ClientError as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def get_recipes(self):
        """This method receives a token and returns the recipes registered in the user account"""
        try:
            response = self.recipe_service.get_recipes()
            response = jsonify(
                recipes = response
            )
            response.status_code = 200
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except ClientError as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def delete_recipe_by_id(self, recipe_id):
        """This method receives a token and a recipe_id and returns a message in case of success"""
        try:
            response = self.recipe_service.delete_recipe_by_id(recipe_id)
            response = jsonify(
                message = "The recipe has been deleted successfully."
            )
            response.status_code = 200
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        
        except RecipeNotFound as err:
            response = jsonify(
                error = str(err)
            )
            response.status_code = 404
            return response
        except ClientError as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def regenerate_recipe(self):
        """This method receives a token and returns a message in case of success"""
        try:
            response = self.recipe_service.regenerate_recipe()
            response = jsonify(
                message = "The recipe has been updated successfully."
            )
            response.status_code = 200
            response.headers.add('Access-Control-Allow-Origin', 'https://gpt-api-frontend.vercel.app')
            return response
        except NoRecipesToUpdate as err:
            response = jsonify(
                error = str(err)
            )
            response.status_code = 422
            return response
        except ClientError as err:
            response = jsonify(
                error = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        