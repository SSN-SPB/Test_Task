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
# 1. Insert Users
# ---------------------------------------------------------

users = [
    ("John", "Smith", "john.smith@email.com", "New York", "2025-01-10"),
    ("Emma", "Johnson", "emma.johnson@email.com", "Chicago", "2025-01-12"),
    (
        "Michael",
        "Brown",
        "michael.brown@email.com",
        "Dallas",
        "2025-01-18",
    ),
    ("Sophia", "Davis", "sophia.davis@email.com", "Seattle", "2025-02-01"),
    ("James", "Wilson", "james.wilson@email.com", "Boston", "2025-02-07"),
    (
        "Olivia",
        "Taylor",
        "olivia.taylor@email.com",
        "Austin",
        "2025-02-15",
    ),
    (
        "Daniel",
        "Anderson",
        "daniel.anderson@email.com",
        "Denver",
        "2025-03-02",
    ),
    ("Emily", "Thomas", "emily.thomas@email.com", "Miami", "2025-03-12"),
    ("David", "Moore", "david.moore@email.com", "Phoenix", "2025-03-20"),
    ("Sarah", "Martin", "sarah.martin@email.com", "Atlanta", "2025-04-01"),
    ("Ryan", "Clark", "ryan.clark@email.com", "Portland", "2025-04-15"),
    (
        "Jessica",
        "White",
        "jessica.white@email.com",
        "San Diego",
        "2025-04-21",
    ),
    ("Kevin", "Hall", "kevin.hall@email.com", "Las Vegas", "2025-05-05"),
    ("Anna", "Lewis", "anna.lewis@email.com", "Nashville", "2025-05-14"),
    (
        "Christopher",
        "Walker",
        "chris.walker@email.com",
        "San Francisco",
        "2025-05-28",
    ),
]


cursor.executemany(
    """
    INSERT INTO shop.Users
        (FirstName, LastName, Email, City, RegistrationDate)
    VALUES (?, ?, ?, ?, ?);
    """,
    users,
)


print(f"Inserted {len(users)} users.")


# ---------------------------------------------------------
# 2. Insert Products
# ---------------------------------------------------------

products = [
    ('Laptop Pro 15"', "Electronics", 1299.99, 15),
    ("Wireless Mouse", "Electronics", 29.99, 120),
    ("Mechanical Keyboard", "Electronics", 89.99, 60),
    ("27-inch Monitor", "Electronics", 279.99, 35),
    ("USB-C Dock", "Accessories", 79.99, 45),
    ("Gaming Headset", "Electronics", 119.99, 40),
    ("External SSD 1TB", "Storage", 149.99, 50),
    ("Office Chair", "Furniture", 249.99, 20),
    ("Standing Desk", "Furniture", 499.99, 12),
    ("Webcam HD", "Electronics", 69.99, 70),
    ("Laser Printer", "Office", 199.99, 18),
    ("Notebook A5", "Office", 4.99, 300),
    ("Gel Pen Set", "Office", 14.99, 250),
    ("Coffee Mug", "Kitchen", 12.99, 100),
    ("Laptop Backpack", "Accessories", 59.99, 80),
]


cursor.executemany(
    """
    INSERT INTO shop.Products
        (ProductName, Category, Price, Stock)
    VALUES (?, ?, ?, ?);
    """,
    products,
)


print(f"Inserted {len(products)} products.")


# ---------------------------------------------------------
# 3. Insert Orders
# ---------------------------------------------------------

orders = [
    (1, 1, 1, "2025-06-01"),
    (2, 2, 2, "2025-06-02"),
    (3, 3, 1, "2025-06-03"),
    (4, 4, 2, "2025-06-04"),
    (5, 8, 1, "2025-06-05"),
    (6, 9, 1, "2025-06-06"),
    (7, 5, 3, "2025-06-07"),
    (8, 6, 1, "2025-06-08"),
    (9, 7, 2, "2025-06-09"),
    (10, 10, 1, "2025-06-10"),
    (11, 11, 1, "2025-06-11"),
    (12, 12, 10, "2025-06-12"),
    (13, 13, 4, "2025-06-13"),
    (14, 14, 2, "2025-06-14"),
    (15, 15, 1, "2025-06-15"),
]


cursor.executemany(
    """
    INSERT INTO shop.Orders
        (UserID, ProductID, Quantity, OrderDate)
    VALUES (?, ?, ?, ?);
    """,
    orders,
)


print(f"Inserted {len(orders)} orders.")


# ---------------------------------------------------------
# 4. Verify Users
# ---------------------------------------------------------

cursor.execute("""
    SELECT *
    FROM shop.Users;
    """)

print("\nUsers:")

for row in cursor.fetchall():
    print(row)


# ---------------------------------------------------------
# 5. Verify Products
# ---------------------------------------------------------

cursor.execute("""
    SELECT *
    FROM shop.Products;
    """)

print("\nProducts:")

for row in cursor.fetchall():
    print(row)


# ---------------------------------------------------------
# 6. Verify Orders
# ---------------------------------------------------------

cursor.execute("""
    SELECT *
    FROM shop.Orders;
    """)

print("\nOrders:")

for row in cursor.fetchall():
    print(row)


# ---------------------------------------------------------
# 7. Cleanup
# ---------------------------------------------------------

cursor.close()
connection.close()

print("\nTest data inserted successfully.")
