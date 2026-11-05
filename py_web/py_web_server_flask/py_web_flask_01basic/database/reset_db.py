import argparse
import os

import pyodbc

DB_SERVER = os.getenv("DB_SERVER", "localhost,1433")
DB_NAME = "TestFlaskServer"
DB_USERNAME = os.getenv("DB_USERNAME", "sa")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")

SEED_USERS = [
    ("John", "Smith", "john.smith@email.com", "New York"),
    ("Emma", "Johnson", "emma.johnson@email.com", "Chicago"),
    ("Michael", "Brown", "michael.brown@email.com", "Dallas"),
    ("Sophia", "Davis", "sophia.davis@email.com", "Seattle"),
    ("James", "Wilson", "james.wilson@email.com", "Boston"),
    ("Olivia", "Taylor", "olivia.taylor@email.com", "Austin"),
    ("Daniel", "Anderson", "daniel.anderson@email.com", "Denver"),
]


def get_connection():
    """Connect to the SQL Server database."""
    if not DB_PASSWORD:
        raise RuntimeError(
            "Set the DB_PASSWORD environment variable before running."
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


def reset_users():
    """Replace all existing users with the original seven seed users."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM testUsers.Users;")

        # Make the next generated UserID equal to 1.
        cursor.execute("DBCC CHECKIDENT ('testUsers.Users', RESEED, 0);")

        cursor.executemany(
            """
            INSERT INTO testUsers.Users
                (FirstName, LastName, Email, City)
            VALUES (?, ?, ?, ?);
            """,
            SEED_USERS,
        )

        connection.commit()

        cursor.execute("""
            SELECT UserID, FirstName, LastName, Email, City
            FROM testUsers.Users
            ORDER BY UserID;
            """)

        rows = cursor.fetchall()

        print(f"Database reset successful. Users found: {len(rows)}")

        for row in rows:
            print(
                f"{row.UserID}: {row.FirstName} {row.LastName} | "
                f"{row.Email} | {row.City}"
            )

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def main():
    parser = argparse.ArgumentParser(
        description="Reset testUsers.Users to the original seven users."
    )
    parser.add_argument(
        "--confirm",
        action="store_true",
        help="Confirm that all existing users may be deleted.",
    )
    args = parser.parse_args()

    if not args.confirm:
        parser.error(
            "This operation deletes all existing users. "
            "Run again with --confirm to proceed."
        )

    reset_users()


if __name__ == "__main__":
    main()
