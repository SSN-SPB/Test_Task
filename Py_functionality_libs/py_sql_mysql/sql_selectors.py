from mysql_service_resources import mysql_connectors as connection


def perform_sql_select(sql_query,
                       print_result=0,
                       schema='test_schema',
                       hostname="localhost"):
    mydb = connection.make_connector(hostname)
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
    return final_list
