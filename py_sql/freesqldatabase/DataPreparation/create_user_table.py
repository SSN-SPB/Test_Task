# pip install mysql-connector-python
import mysql.connector
import os

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
        database=DB_NAME
    )

    if conn.is_connected():
        print("Connected to the database!")

    cursor = conn.cursor()

    # Create a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    cursor.execute(create_table_query)
    print("Table 'users' created successfully!")

    # Close connection
    cursor.close()
    conn.close()
    print("Connection closed.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
