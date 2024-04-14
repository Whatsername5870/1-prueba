import psycopg2

class PostgreDatabase:
    def __init__(
            self, database: str ="db_name", host: str = "db_host",
            user: str = "db_user", password: str = "db_password", port: int = 5432
    ) -> None:
        self.conn = psycopg2.connect(
            database=database, host=host, user=user, password=password, port=port
        )