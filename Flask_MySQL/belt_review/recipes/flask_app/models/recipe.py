from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask import flash
import re
from flask_app.models import user

class Recipe:
    def __init__(self,data):
        self.id = data["id"]
        self.made_on = data["made_on"]
        self.under_30 = data["under_30"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users_id = data["users_id"]
    
    @classmethod
    def new_recipe(cls,data):
        query = "INSERT INTO recipes (name, made_on, under_30, description, instructions) VALUES (%(name)s, %(made_on)s, %(under_30)s, %(description)s, %(instructions)s)"
        return connectToMySQL("users_recipes_schema").query_db(query,data)
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data["name"]) < 3:
            flash("Name is required.")
            is_valid = False
        if len(data["description"]) < 3:
            flash("Description is required.")
            is_valid = False
        if len(data["instructions"]) < 3:
            flash("Instructions are required.")
            is_valid = False
        return is_valid