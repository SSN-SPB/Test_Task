import os

import pyodbc

SERVER = os.getenv("DB_SERVER", "localhost,1433")
DATABASE = "TestFlaskServer"
USERNAME = os.getenv("DB_USERNAME", "sa")
PASSWORD = os.getenv("DB_PASSWORD")

DRIVER = "ODBC Driver 18 for SQL Server"


def get_connection_string(database):
    if not PASSWORD:
        raise RuntimeError(
            "Set the DB_PASSWORD environment variable before running."
        )

    return (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={database};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )


def create_database():
    # Connect to master because TestFlaskServer may not exist yet.
    connection = pyodbc.connect(
        get_connection_string("master"),
        autocommit=True,
    )

    try:
        cursor = connection.cursor()

        cursor.execute("""
            IF DB_ID(N'TestFlaskServer') IS NULL
            BEGIN
                CREATE DATABASE TestFlaskServer;
            END;
        """)

        print(f"Database '{DATABASE}' is ready.")

    finally:
        connection.close()


def create_schema_and_table(cursor):
    cursor.execute("""
        IF SCHEMA_ID(N'testUsers') IS NULL
        BEGIN
            EXEC(N'CREATE SCHEMA testUsers');
        END;

        IF OBJECT_ID(N'testUsers.Users', N'U') IS NULL
        BEGIN
            CREATE TABLE testUsers.Users
            (
                UserID INT IDENTITY(1,1) PRIMARY KEY,
                FirstName NVARCHAR(50) NOT NULL,
                LastName NVARCHAR(50) NOT NULL,
                Email NVARCHAR(100) UNIQUE NOT NULL,
                City NVARCHAR(50)
            );
        END;
    """)


def seed_users(cursor):
    cursor.execute("""
        IF NOT EXISTS (
            SELECT 1
            FROM testUsers.Users
        )
        BEGIN
            INSERT INTO testUsers.Users
                (FirstName, LastName, Email, City)
            VALUES
                ('John', 'Smith',
                 'john.smith@email.com', 'New York'),
                ('Emma', 'Johnson',
                 'emma.johnson@email.com', 'Chicago'),
                ('Michael', 'Brown',
                 'michael.brown@email.com', 'Dallas'),
                ('Sophia', 'Davis',
                 'sophia.davis@email.com', 'Seattle'),
                ('James', 'Wilson',
                 'james.wilson@email.com', 'Boston'),
                ('Olivia', 'Taylor',
                 'olivia.taylor@email.com', 'Austin'),
                ('Daniel', 'Anderson',
                 'daniel.anderson@email.com', 'Denver');
        END;
    """)


def verify_users(cursor):
    cursor.execute("""
        SELECT UserID, FirstName, LastName, Email, City
        FROM testUsers.Users
        ORDER BY UserID;
    """)

    rows = cursor.fetchall()

    print(f"\nUsers found: {len(rows)}")
    for row in rows:
        print(
            f"{row.UserID}: {row.FirstName} {row.LastName} | "
            f"{row.Email} | {row.City}"
        )


def main():
    create_database()

    connection = pyodbc.connect(get_connection_string(DATABASE))

    try:
        cursor = connection.cursor()

        create_schema_and_table(cursor)
        seed_users(cursor)

        connection.commit()

        verify_users(cursor)

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


if __name__ == "__main__":
    main()
