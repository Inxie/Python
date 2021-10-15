from flask_app.config.mysqlconnection import connectToMySQL

class Dojos:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        @classmethod
        def all_dojos(cls):
            query = "SELECT * FROM dojos ORDER BY id DESC"
            db_dojos = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
            dojos = []

            for d in db_dojos:
                dojos.append(Dojos(d))
            
            return dojos

class Ninjas:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.ag = data["ag"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]