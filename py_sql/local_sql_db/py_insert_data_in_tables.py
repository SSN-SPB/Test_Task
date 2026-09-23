import os

import pyodbc
from dotenv import load_dotenv

load_dotenv()


SERVER = os.environ["DB_SERVER"]
USERNAME = os.environ["DB_USERNAME"]
PASSWORD = os.environ["DB_PASSWORD"]
DATABASE = "master"


connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    "TrustServerCertificate=yes;"
)


def execute_query(cursor, query):
    print(f"\nExecuting:\n{query.strip()}")
    cursor.execute(query)


connection = pyodbc.connect(connection_string, autocommit=True)
cursor = connection.cursor()


# ---------------------------------------------------------
# 1. SQL Server version
# ---------------------------------------------------------

cursor.execute("SELECT @@VERSION;")

version = cursor.fetchone()[0]

print("\nSQL Server version:")
print(version)


# ---------------------------------------------------------
# 2. Create database
# ---------------------------------------------------------

execute_query(
    cursor,
    """
    IF DB_ID('ShopDB') IS NULL
        CREATE DATABASE ShopDB;
    """,
)


# ---------------------------------------------------------
# 3. Connect to ShopDB
# ---------------------------------------------------------

connection.close()

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE=ShopDB;"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    "TrustServerCertificate=yes;"
)

connection = pyodbc.connect(connection_string, autocommit=True)
cursor = connection.cursor()


# ---------------------------------------------------------
# 4. Check current database
# ---------------------------------------------------------

cursor.execute("SELECT DB_NAME() AS CurrentDatabase;")

current_database = cursor.fetchone()[0]

print(f"\nCurrent database: {current_database}")


# ---------------------------------------------------------
# 5. Show existing schemas
# ---------------------------------------------------------

cursor.execute("""
    SELECT name
    FROM sys.schemas
    ORDER BY name;
    """)

print("\nExisting schemas:")

for row in cursor.fetchall():
    print(row.name)


# ---------------------------------------------------------
# 6. Create shop schema
# ---------------------------------------------------------

execute_query(
    cursor,
    """
    IF NOT EXISTS (
        SELECT 1
        FROM sys.schemas
        WHERE name = 'shop'
    )
        EXEC('CREATE SCHEMA shop');
    """,
)


# ---------------------------------------------------------
# 7. Create Users table
# ---------------------------------------------------------

execute_query(
    cursor,
    """
    IF OBJECT_ID('shop.Users', 'U') IS NULL
    BEGIN
        CREATE TABLE shop.Users
        (
            UserID INT IDENTITY(1,1) PRIMARY KEY,
            FirstName NVARCHAR(50) NOT NULL,
            LastName NVARCHAR(50) NOT NULL,
            Email NVARCHAR(100) UNIQUE NOT NULL,
            City NVARCHAR(50),
            RegistrationDate DATE DEFAULT GETDATE()
        );
    END
    """,
)


# ---------------------------------------------------------
# 8. Create Products table
# ---------------------------------------------------------

execute_query(
    cursor,
    """
    IF OBJECT_ID('shop.Products', 'U') IS NULL
    BEGIN
        CREATE TABLE shop.Products
        (
            ProductID INT IDENTITY(1,1) PRIMARY KEY,
            ProductName NVARCHAR(100) NOT NULL,
            Category NVARCHAR(50),
            Price DECIMAL(10,2),
            Stock INT
        );
    END
    """,
)


# ---------------------------------------------------------
# 9. Create Orders table
# ---------------------------------------------------------

execute_query(
    cursor,
    """
    IF OBJECT_ID('shop.Orders', 'U') IS NULL
    BEGIN
        CREATE TABLE shop.Orders
        (
            OrderID INT IDENTITY(1,1) PRIMARY KEY,
            UserID INT NOT NULL,
            ProductID INT NOT NULL,
            Quantity INT,
            OrderDate DATE,

            CONSTRAINT FK_Orders_User
                FOREIGN KEY (UserID)
                REFERENCES shop.Users(UserID),

            CONSTRAINT FK_Orders_Product
                FOREIGN KEY (ProductID)
                REFERENCES shop.Products(ProductID)
        );
    END
    """,
)


# ---------------------------------------------------------
# 10. Verify tables
# ---------------------------------------------------------

cursor.execute("""
    SELECT TABLE_SCHEMA, TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'shop'
    ORDER BY TABLE_NAME;
    """)

print("\nTables in shop schema:")

for row in cursor.fetchall():
    print(f"{row.TABLE_SCHEMA}.{row.TABLE_NAME}")


# ---------------------------------------------------------
# 11. Cleanup
# ---------------------------------------------------------

cursor.close()
connection.close()

print("\nDatabase setup completed successfully.")
