from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojos:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos ORDER BY id ASC"
        get_all_dojos = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []
        
        for d in get_all_dojos:
            dojos.append(Dojos(d))
        
        return dojos
    
    @classmethod
    def new_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
    
    # @classmethod
    # def one_dojo(cls):
    #     query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id"
    #     one_dojo_ninjas = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
    #     dojos_and_ninjas_schema = []

    #     for ninja1 in one_dojo_ninjas:
    #         ninjas_instance = Dojos(ninja1)

    #         ninjas_data = {
    #             "id": ninja1["id"],
    #             "first_name": ninja1["first_name"],
    #             "last_name": ninja1["last_name"],
    #             "age": ninja1["age"],
    #             "created_at": ninja1["created_at"],
    #             "updated_at": ninja1["updated_at"],
    #             "dojo_id" : ninja1["dojo_id"]
    #         }
    #         ninjas_instance.ninja = ninja.Ninjas(ninjas_data)

    #         dojos_and_ninjas_schema.ninjas.append(ninjas_instance)

    #     return dojos_and_ninjas_schema
    
    # @classmethod
    # def all_ninjas(cls):
    #     query = "SELECT * FROM dojos JOIN ninjas ON dojos.id=ninjas.id ORDER BY id DESC"
    #     db_ninjas = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
    #     ninjas = []

    #     for n in db_ninjas:
    #         ninjas.append(Dojos(n))
        
    #     return ninjas