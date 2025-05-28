#!/usr/bin/env python3

import mysql.connector
import os


def main_mysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user=os.environ.get("MYSQL_TEST_USER"),
        password=os.environ.get("MYSQL_TEST_USER_PASS"),
    )

    print(mydb)
    # print(type(mydb))
    # print(dir(mydb))
    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)


if __name__ == "__main__":
    main_mysql()
