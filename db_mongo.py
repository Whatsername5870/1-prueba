from pymongo import MongoClient

class MongoDB:
    def __init__(self, host: str = "localhost", port: int = 27017, usernamen: str = "root", password: str = "example") -> None:
        self.client = MongoClient(host=host, port=port, username=usernamen, password=password)
        self.db = self.client["encuestas"]
        self.respuestas_collection = self.db["respuestas"]