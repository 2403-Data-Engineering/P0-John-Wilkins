import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host = os.getenv("HOST")
            user = os.getenv("USER")
            password = os.getenv("PASSWORD")
            port = os.getenv("PORT")
            db = os.getenv("DB")
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None