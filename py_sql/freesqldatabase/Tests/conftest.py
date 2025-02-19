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
