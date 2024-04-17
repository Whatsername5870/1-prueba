from db_postgre import PostgreDatabase

class PostgreDatabaseService:
    def __init__(self, database: PostgreDatabase) -> None:
        self.database = database
    
    # ----------------- Consultas ----------------- #
    
    def query_prueba(self) -> list:
        return self.database.query_prueba()
    
    # ----------------- Inserciones ----------------- #

    def insertar_user(self, user: dict) -> dict:
        return self.database.insert_user(user)