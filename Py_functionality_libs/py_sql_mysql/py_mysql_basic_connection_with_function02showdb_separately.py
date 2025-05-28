#!/usr/bin/env python3
import mysql.connector
import os


def get_list_of_schemes(hostname="localhost"):
    mydb = mysql.connector.connect(
        host=hostname,
        user=os.environ.get("MYSQL_TEST_USER"),
        password=os.environ.get("MYSQL_TEST_USER_PASS"),
    )

    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    myresult = cursor.fetchall()

    final_list = []

    for x in myresult:
        final_list.append(x[0])
    print(final_list)
    return final_list


def perform_sql_select(
    sql_querry, print_result=0, schema="test_schema", hostname="localhost"
):
    mydb = mysql.connector.connect(
        host=hostname,
        user=os.environ.get("MYSQL_TEST_USER"),
        password=os.environ.get("MYSQL_TEST_USER_PASS"),
    )
    cursor = mydb.cursor()
    cursor.execute("USE " + schema)
    cursor.execute(sql_querry)
    myresult = cursor.fetchall()
    final_list = []
    for x in myresult:
        final_list.append(list(x))
    if print_result:
        for x in final_list:
            print(x)
    return final_list


def main_mysql():
    print(os.environ.get("MYSQL_TEST_USER"))
    print(os.environ.get("MYSQL_TEST_USER_PASS"))
    list_of_db = get_list_of_schemes()
    print(list_of_db[0])
    perform_sql_select("show tables", schema=list_of_db[0], print_result=0)
    perform_sql_select(
        "SELECT * FROM CHARACTER_SETS", schema=list_of_db[0], print_result=1
    )


if __name__ == "__main__":
    main_mysql()
