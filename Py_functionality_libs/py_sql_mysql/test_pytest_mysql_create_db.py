#!/usr/bin/env python3
import mysql.connector
import os


def get_list_of_schemes(hostname="localhost", print_result=0):
    mydb = mysql.connector.connect(
        host=hostname,
        user=os.environ.get('MYSQL_ADMIN'),
        password=os.environ.get('MYSQL_ADMIN_PASSWORD')
        )

    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    action_result = cursor.fetchall()

    final_list = []

    for x in action_result:
        final_list.append(x[0])
    if print_result:
        print(final_list)
    return final_list


def perform_sql_select(sql_query, print_result=0,
                       schema='test_schema',
                       hostname="localhost"):
    mydb = mysql.connector.connect(
        host=hostname,
        user=os.environ.get('MYSQL_TEST_USER'),
        password=os.environ.get('MYSQL_TEST_USER_PASS')
        )
    if print_result:
        print(mydb)
    cursor = mydb.cursor()
    cursor.execute("USE " + schema)
    cursor.execute(sql_query)
    action_result = cursor.fetchall()
    final_list = []
    for x in action_result:
        final_list.append(list(x))
    if print_result:
        for x in final_list:
            print(x)
    return final_list


def make_action_with_db(tested_schema,
                        action_with_db="create",
                        hostname="localhost",
                        print_result=0):
    mydb = mysql.connector.connect(
        host=hostname,
        user=os.environ.get('MYSQL_ADMIN'),
        password=os.environ.get('MYSQL_ADMIN_PASSWORD')
        )
    cursor = mydb.cursor()
    sql_string = action_with_db + " database " + tested_schema
    if print_result:
        print(sql_string)
    cursor.execute(sql_string)
    cursor.fetchall()


def check_if_schema_exists(tested_schema, hostname="localhost"):
    mydb = mysql.connector.connect(
        host=hostname,
        user=os.environ.get('MYSQL_ADMIN'),
        password=os.environ.get('MYSQL_ADMIN_PASSWORD')
        )

    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    action_result = cursor.fetchall()
    for x in action_result:
        if tested_schema == x[0]:
            print('schema is found')
            return True
    return False


def test_check_schema_creating_mysql():
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
    make_action_with_db("auto", action_with_db="drop", hostname="localhost")
    print("restoring the initial list of databases")
    restored_list_of_db = get_list_of_schemes()
    assert "auto" not in restored_list_of_db
    print(restored_list_of_db)


if __name__ == '__main__':
    test_check_schema_creating_mysql()
