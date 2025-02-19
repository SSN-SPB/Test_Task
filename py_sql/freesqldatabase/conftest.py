import pytest
import os
import mysql.connector

DB_HOST = "sql7.freesqldatabase.com"
DB_NAME = "sql7763341"
DB_USER = "sql7763341"
DB_PASS = os.environ.get("freedb_user_password")
PORT = "3306"

@pytest.fixture
def setup_data():
    DB_HOST = "sql7.freesqldatabase.com"
    DB_NAME = "sql7763341"
    DB_USER = "sql7763341"
    DB_PASS = os.environ.get("freedb_user_password")
    PORT = "3306"
    return locals()


@pytest.fixture()
def get_db_connector(setup_data):
    try:
        conn = mysql.connector.connect(
            # host=DB_HOST,
            # user=DB_USER,
            # password=DB_PASS,
            # database=DB_NAME
            host=setup_data["DB_HOST"],
            user=setup_data["DB_USER"],
            password=setup_data["DB_PASS"],
            database=setup_data["DB_NAME"]
        )

        if conn.is_connected():
            print("Connected to the database!")

        cursor = conn.cursor()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return conn, cursor