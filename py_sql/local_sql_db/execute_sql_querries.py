import os

import pyodbc
from dotenv import load_dotenv

load_dotenv()


SERVER = os.environ["DB_SERVER"]
USERNAME = os.environ["DB_USERNAME"]
PASSWORD = os.environ["DB_PASSWORD"]
DATABASE = os.environ["DB_DATABASE"]


connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    "TrustServerCertificate=yes;"
)


connection = pyodbc.connect(
    connection_string,
    autocommit=True,
)

cursor = connection.cursor()


# ---------------------------------------------------------
# 1. Summary query
# ---------------------------------------------------------

cursor.execute("""
SELECT
    o.OrderID,
    u.FirstName + ' ' + u.LastName AS Customer,
    p.ProductName,
    p.Category,
    o.Quantity,
    p.Price,
    o.Quantity * p.Price AS TotalPrice,
    o.OrderDate
FROM shop.Orders AS o
JOIN shop.Users AS u
    ON o.UserID = u.UserID
JOIN shop.Products AS p
    ON o.ProductID = p.ProductID
ORDER BY o.OrderID;
    """)

print("\nOrders:")

for row in cursor.fetchall():
    print(row)


# ---------------------------------------------------------
# 2. Cleanup
# ---------------------------------------------------------

cursor.close()
connection.close()

print("\nTest data retrieved successfully.")
