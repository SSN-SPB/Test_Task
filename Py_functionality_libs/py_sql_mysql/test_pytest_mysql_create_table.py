#!/usr/bin/env python3
import pytest
from mysql_service_resources import mysql_connectors as connection
import sql_selectors as query


def get_list_of_schemes(hostname="localhost", print_result=0):
    mydb = connection.make_connector(hostname)
    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    action_result = cursor.fetchall()

    final_list = []

    for x in action_result:
        final_list.append(x[0])
    if print_result:
        print(final_list)
    return final_list


def make_action_with_db(tested_schema,
                        action_with_db="create",
                        hostname="localhost",
                        print_result=0):
    mydb = connection.make_connector(hostname)
    cursor = mydb.cursor()
    sql_string = action_with_db + " database " + tested_schema
    if print_result:
        print(sql_string)
    cursor.execute(sql_string)
    cursor.fetchall()


def check_if_schema_exists(tested_schema, hostname="localhost"):
    mydb = connection.make_connector(hostname)
    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    action_result = cursor.fetchall()
    for x in action_result:
        if tested_schema == x[0]:
            print('schema is found')
            return True
    return False


@pytest.fixture(scope='class', autouse=False)
def setup():
    check_if_schema_exists("auto")
    print("The initial list of databases")
    get_list_of_schemes(print_result=1)
    try:
        make_action_with_db("auto", hostname="localhost")
    except Exception as general_exception:
        print(general_exception)
        print("The tested Database exists already")
    print("The updated list of databases")
    updated_schema_list = get_list_of_schemes(print_result=1)
    assert "auto" in updated_schema_list


@pytest.fixture()
def introduction():
    print('Start pytest')
    yield
    print("restoring the initial list of databases")
    make_action_with_db("auto",
                        action_with_db="drop",
                        hostname="localhost")
    restored_list_of_schemas = get_list_of_schemes()
    assert "auto" not in restored_list_of_schemas
    print(restored_list_of_schemas)
    print('Test is finished')


@pytest.mark.usefixtures('introduction', 'setup')
def test_check_table_creating_mysql():
    query.perform_sql_select("show tables",
                             print_result=1,
                             schema='auto',
                             hostname="localhost")
    create_table_sql_query = "CREATE TABLE cars ("\
                             " id INT AUTO_INCREMENT,"\
                             " make VARCHAR(100) NOT NULL,"\
                             " model VARCHAR(100) NOT NULL,"\
                             " PRIMARY KEY (id))"
    query.perform_sql_select(create_table_sql_query,
                             print_result=1,
                             schema='auto')
    query.perform_sql_select("show tables",
                             print_result=1,
                             schema='auto',
                             hostname="localhost")


if __name__ == '__main__':
    check_if_schema_exists("auto")
    print("The initial list of databases")
    get_list_of_schemes(print_result=1)
    try:
        make_action_with_db("auto", hostname="localhost")
    except Exception as e:
        print(e)
        print("The tested Database exists already")
    print("The updated list of databases")
    updated_list = get_list_of_schemes(print_result=1)
    assert "auto" in updated_list
    test_check_table_creating_mysql()
    print("restoring the initial list of databases")
    make_action_with_db("auto",
                        action_with_db="drop",
                        hostname="localhost")
    restored_list_of_db = get_list_of_schemes()
    assert "auto" not in restored_list_of_db
    print(restored_list_of_db)
    print('Test is finished')
