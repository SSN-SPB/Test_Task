#!/usr/bin/env python3

import mysql.connector
import os


def perform_sql_select(sql_querry):
    mydb = mysql.connector.connect(
        host="localhost",
        user=os.environ.get('MYSQL_TEST_USER'),
        password=os.environ.get('MYSQL_TEST_USER_PASS')
        )

    print(mydb)
    cursor = mydb.cursor()
    cursor.execute("USE information_schema")
    cursor.execute(sql_querry)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)


def main_mysql():
    perform_sql_select("SHOW DATABASES")
    perform_sql_select("show tables")


if __name__ == '__main__':
    main_mysql()
