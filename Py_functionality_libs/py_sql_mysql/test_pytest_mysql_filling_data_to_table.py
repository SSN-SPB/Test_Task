#!/usr/bin/env python3
from mysql_service_resources.mysql_requests import *
from mysql_service_resources.pytest_service_fixtures import *


CREATE_TABLE_SQL = "CREATE TABLE cars (" \
                   " id INT AUTO_INCREMENT," \
                   " make VARCHAR(100) NOT NULL," \
                   " model VARCHAR(100) NOT NULL," \
                   " PRIMARY KEY (id))"


@pytest.mark.usefixtures('introduction', 'setup')
def test_check_table_creating_mysql():
    step1 = "To check the initial list of tables"
    step2 = "Create new table"
    step3 = "To check the updated list of tables"
    perform_sql_select("show tables",
                       target_of_select=step1,
                       print_result=1,
                       schema='auto',
                       hostname="localhost")
    perform_sql_select(CREATE_TABLE_SQL,
                       target_of_select=step2,
                       print_result=0,
                       schema='auto')
    perform_sql_select("show tables",
                       target_of_select=step3,
                       print_result=1,
                       schema='auto',
                       hostname="localhost")


if __name__ == '__main__':
    print("The python test")
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
