# pip install mysql-connector-python
# import mysql.connector
import logging
from ..ServiceModules import sql_querries as query
from ..ServiceModules import connectors
logger = logging.getLogger(__name__)


def test_show_tables(setup_data):
    show_table_users = query.retrieve_user_data["show_table_users"]
    connection, current_cursor = connectors.get_connectors(setup_data)

    current_cursor.execute(show_table_users)
    users = current_cursor.fetchall()
    logger.info(users)
    assert users is not None
    assert users[0] == (2, 'John Doe')
    logger.info(connectors.close_connectors(connection, current_cursor))

