from mysql_service_resources.mysql_connectors import *


def get_list_of_schemes(hostname="localhost", print_result=0):
    mydb = make_connector(hostname)
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
    mydb = make_connector(hostname)
    cursor = mydb.cursor()
    sql_string = action_with_db + " database " + tested_schema
    if print_result:
        print(sql_string)
    cursor.execute(sql_string)
    cursor.fetchall()


def check_if_schema_exists(tested_schema, hostname="localhost"):
    mydb = make_connector(hostname)
    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")
    action_result = cursor.fetchall()
    for x in action_result:
        if tested_schema == x[0]:
            print('schema is found')
            return True
    return False


def perform_sql_select(sql_query,
                       target_of_select='',
                       print_result=0,
                       schema='test_schema',
                       hostname="localhost"):
    mydb = make_connector(hostname)
    print(target_of_select)
    if print_result:
        print("The requested query is: '{}'".format(sql_query))
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
        if not final_list:
            print('No data is found')
            print('The list is {}'.format(final_list))
    return final_list
