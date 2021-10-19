from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask import flash
from flask_app.models import recipe
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.recipes = []
    
    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if len(data['email']) < 1:
            flash("Email cannot be blank.")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address.")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if data["confirm_password"] != (data["password"]):
            flash("Passwords must match.")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, confirm_password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(confirm_password)s)"
        return connectToMySQL("users_recipes_schema").query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL("users_recipes_schema").query_db(query,data)
        users = []
        for one in results:
            users.append(User(one))
        return users
    
    @classmethod
    def check_by_id(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL("users_recipes_schema").query_db(query,data)
        return User(results[0])

    @classmethod
    def check_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("users_recipes_schema").query_db(query,data)
        if len(results) < 1:
            return False
        return User(results[0])
    
    @classmethod
    def one_recipe(cls,data):
        print(data)
        query = f"SELECT * FROM recipes WHERE id={data.get('recipe_id')} LIMIT 1"
        requested_recipe = connectToMySQL("users_recipes_schema").query_db(query,data)
        the_recipe = requested_recipe[0]
        return the_recipe