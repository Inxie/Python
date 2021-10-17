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
    # def one_dojo_ninjas(cls):
    #     query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id"
    #     one_dojo_ninjas = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
    #     dojos_ninjas_both = []

    #     for dojosninjas in one_dojo_ninjas:
    #         ninjas_instance = Dojos(dojosninjas)

    #         ninjas_data = {
    #             "id": dojosninjas["id"],
    #             "first_name": dojosninjas["first_name"],
    #             "last_name": dojosninjas["last_name"],
    #             "age": dojosninjas["age"],
    #             "created_at": dojosninjas["created_at"],
    #             "updated_at": dojosninjas["updated_at"],
    #             "dojo_id" : dojosninjas["dojo_id"]
    #         }
    #         ninjas_instance.ninja = ninja.Ninjas(ninjas_data)

    #         dojos_ninjas_both.append(ninjas_instance)

    #     return dojos_ninjas_both

    @classmethod
    def one_dojos_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE ninjas.dojo_id = %(id)s"
        all_dojos_ninjas = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        
        dojo_one = Dojos(all_dojos_ninjas[0])

        for dojosninjas in all_dojos_ninjas:
            ninjas_data = {
                "id": dojosninjas["id"],
                "first_name": dojosninjas["first_name"],
                "last_name": dojosninjas["last_name"],
                "age": dojosninjas["age"],
                "created_at": dojosninjas["created_at"],
                "updated_at": dojosninjas["updated_at"],
                "dojo_id" : dojosninjas["dojo_id"]
            }

            dojo_one.ninjas.append(ninja.Ninjas(ninjas_data))

        return dojo_one

