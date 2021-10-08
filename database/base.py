"""Make new database"""

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# make db (students_db)

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1111",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    sql_create_db = 'create database students_db'
    cursor.execute(sql_create_db)
except (Exception, Error) as error:
    print(error)
finally:
    if connection:
        cursor.close()
        connection.close()