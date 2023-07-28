"""Translator controller"""
from marshmallow import ValidationError
from mysql.connector import Error
from flask import jsonify, request

class TranslatorController:
    """This class receives data from the HTTP request and returns the response"""

    def __init__(self, translator_service):
        self.translator_service = translator_service
         
    def create_translation(self):
        """This method receives a source language, a target language and a text and sends it to the service layer"""
        try:
            data = request.json
            response = self.translator_service.create_translation(data)

            response = jsonify(
                message = "The translation has been registered successfully",
                data = response
            )
            response.status_code = 201
            return response
    
        except ValidationError as err:
            response = jsonify(
                message = f"Validation error: {err}"
            )
            response.status_code = 422
            return response
    
        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response

    def get_translations(self):
        """This method receives a token and sends it to the service layer"""
        try:
            response = self.translator_service.get_translations()
            
            response = jsonify(
                translations = response
            )
            
            response.status_code = 200
            return response
        
        except Error as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response