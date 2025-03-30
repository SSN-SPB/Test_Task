import mysql.connector
from os import environ as env


def make_connector(hostname):
    mydb = mysql.connector.connect(host=hostname,
                                   user=env.get('MYSQL_ADMIN'),
                                   password=env.get('MYSQL_ADMIN_PASSWORD')
                                   )
    return mydb