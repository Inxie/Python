from mysqlconnection import connectToMySQL

class Users:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def insert_new(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL("users_schema").query_db(query,data)

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users ORDER BY id DESC"
        db_users = connectToMySQL("users_schema").query_db(query)
        users = []

        for u in db_users:
            users.append(Users(u))
        
        return users