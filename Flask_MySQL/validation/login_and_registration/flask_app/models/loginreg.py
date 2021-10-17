from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Register:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @staticmethod
    def validate_registration(data):
        is_valid = True # we assume this is true
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
            flash("Invalid email address!")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if data["confirm_password"] != (data["password"]):
            flash("Passwords must match.")
            is_valid = False
        return is_valid

    @classmethod
    def save_registration(cls,data):
        query = "INSERT INTO accounts (first_name, last_name, email, password, confirm_password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(confirm_password)s)"
        return connectToMySQL("login_and_registration_schema").query_db(query,data)
    
    @classmethod
    def check_by_email(cls,data):
        query = "SELECT * FROM accounts WHERE email = %(email)s;"
        result = connectToMySQL("login_and_registration_schema").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])