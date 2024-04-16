from db_mongo import MongoDB

class MongoDatabaseService:
    def __init__(self, database: MongoDB) -> None:
        self.database = database
    
    # ----------------- Logic ----------------- #