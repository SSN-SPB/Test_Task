# pip install mysql-connector-python
# import mysql.connector
import logging

from py_sql.freesqldatabase.ServiceModules import sql_querries as query
from py_sql.freesqldatabase.ServiceModules import connectors
logger = logging.getLogger(__name__)


def test_show_tables(setup_data):
    show_table_query = query.retrieve_table_data["show_tables"]
    connection, current_cursor = connectors.get_connectors(setup_data)

    current_cursor.execute(show_table_query)
    tables = current_cursor.fetchall()
    logger.info(tables)
    assert tables[0][0] == "orders"
    logger.info(connectors.close_connectors(connection, current_cursor))

