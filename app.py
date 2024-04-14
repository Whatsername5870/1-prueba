import os

from flask import Flask, request
from db_postgre import PostgreDatabase
from db_postgre_service import PostgreDatabaseService

POSTGRES_DB_HOST = os.getenv('POSTGRES_DB_HOST')
POSTGRES_DB_NAME = os.getenv('POSTGRES_DB_NAME')
POSTGRES_DB_USER = os.getenv('POSTGRES_DB_USER')
POSTGRES_DB_PASSWORD = os.getenv('POSTGRES_DB_PASSWORD')
POSTGRES_DB_PORT = os.getenv('POSTGRES_DB_PORT')

postgre_db = PostgreDatabase(database=POSTGRES_DB_NAME, host=POSTGRES_DB_HOST,
                                user=POSTGRES_DB_USER, password=POSTGRES_DB_PASSWORD,
                                port=POSTGRES_DB_PORT)

app = Flask(__name__)
postgre_db_service = PostgreDatabaseService(database=postgre_db)

@app.route('/')
def home():
    return 'Hello, World!'