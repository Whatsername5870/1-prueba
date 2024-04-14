from db_postgre import PostgreDatabase

class PostgreDatabaseService:
    def __init__(self, database: PostgreDatabase) -> None:
        self.database = database
    
    # ----------------- Logic ----------------- #