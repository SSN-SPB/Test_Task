# pip install mysql-connector-python
import mysql.connector
import os

# Replace these with your database credentials
DB_HOST = "sql7.freesqldatabase.com"
DB_NAME = "sql7763341"
DB_USER = "sql7763341"
# DB_PASS = "TyF16vPCeR"
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

    cursor.execute("SELECT DATABASE();")
    print("Connected to database:", cursor.fetchone()[0])

    # Insert record
    insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    # record = ("John Doe", "johndoe@example.com")
    record = ("Smith2", "smith2@example.com")

    cursor.execute(insert_query, record)
    print(f"Rows affected: {cursor.rowcount}")

    # Verify last inserted ID
    cursor.execute("SELECT LAST_INSERT_ID();")
    print("Last inserted ID:", cursor.fetchone()[0])

    # Close connection
    cursor.close()
    conn.close()
    print("Connection closed.")

except mysql.connector.Error as err:
    print(f"Error: {err}")