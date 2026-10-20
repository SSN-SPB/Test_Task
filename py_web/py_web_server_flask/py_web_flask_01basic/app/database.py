
import os

import pyodbc


DB_SERVER = os.getenv("DB_SERVER", "localhost,1433")
DB_NAME = os.getenv("DB_NAME", "TestFlaskServer")
DB_USERNAME = os.getenv("DB_USERNAME", "sa")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")


def get_connection():
    """Create and return a SQL Server database connection."""
    if not DB_PASSWORD:
        raise RuntimeError(
            "The DB_PASSWORD environment variable is not set."
        )

    connection_string = (
        f"DRIVER={{{DB_DRIVER}}};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_NAME};"
        f"UID={DB_USERNAME};"
        f"PWD={DB_PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(connection_string)


def get_all_users():
    """Return all users from the testUsers.Users table."""
    query = """
        SELECT UserID, FirstName, LastName, Email, City
        FROM testUsers.Users
        ORDER BY UserID;
    """

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)

        column_names = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        return [
            dict(zip(column_names, row))
            for row in rows
        ]
