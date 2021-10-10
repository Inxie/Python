# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Users:
    def __init__(self):
        self.id = ['id']
        self.first_name = ['first_name']
        self.last_name = ['last_name']
        self.email = ['email']
        self.created_at = ['created_at']
        self.updated_at = ['updated_at']

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        Users = []
        # Iterate over the db results and create instances of friends with cls.
        for Users in results:
            users.append(cls(Users))
        return Users