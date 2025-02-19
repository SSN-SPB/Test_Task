# pip install mysql-connector-python
import mysql.connector
import os
from ServiceModules import sql_querries as querry
from ServiceModules import connectors

# Connectin credentials
DB_HOST = "sql7.freesqldatabase.com"
DB_NAME = "sql7763341"
DB_USER = "sql7763341"
DB_PASS = os.environ.get("freedb_user_password")
PORT = "3306"

# Connect to the database
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

    if conn.is_connected():
        print("Connected to the database!")

    cursor = conn.cursor()

    # Get the list of tables
    show_table_query = querry.retrieve_table_data["show_tables"]

    cursor.execute(show_table_query)
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    connectors.close_connectors(conn, cursor)

except mysql.connector.Error as err:
    print(f"Error: {err}")