# pip install mysql-connector-python
import mysql.connector
import os
from ServiceModules import sql_querries as querry
from ServiceModules import connectors

# Replace these with your database credentials
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
        database=DB_NAME,
        autocommit=True
    )

    if conn.is_connected():
        print("Connected to the database!")

    cursor = conn.cursor()

    show_table_users = "select u.id as uid, u.name from users u"

    cursor.execute(show_table_users)
    tables = cursor.fetchall()
    print(f"Tables in the database: {tables}")
    for table in tables:
        print(table[0])

    # Close connection
    # cursor.close()
    # conn.close()
    connectors.close_connectors(conn, cursor)
    print("Connection closed.")

except mysql.connector.Error as err:
    print(f"Error: {err}")