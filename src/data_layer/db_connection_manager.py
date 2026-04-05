# import os
# import mysql.connector
# from dotenv import load_dotenv

# load_dotenv()

# def get_db_connection():
#     try:
#         connection = mysql.connector.connect(
#             host = os.getenv("HOST")
#             user = os.getenv("USER")
#             password = os.getenv("PASSWORD")
#             port = os.getenv("PORT")
#             database = os.getenv("DB")
#         )
#         return connection
#     except mysql.connector.Error as err:
#         print(f"Error connecting to the database: {err}")
#         return None
import mysql.connector
import os


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DB"),
        port=int(os.getenv("PORT", 3306))
    )