#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

con = None

try:
    connection_string = "host='localhost' " \
                        "port='5432' " \
                        "dbname='postgres' " \
                        "user='postgres' " \
                        "password='postgres'"
    conn = psycopg2.connect(connection_string)

    cur = conn.cursor()
    cur.execute("DELETE FROM Products WHERE Id=" + str(4))

    conn.commit()

except psycopg2.DatabaseError as e:
    if conn:
        conn.rollback()

    print('Error %s' % e)
    sys.exit(1)

finally:
    if conn:
        conn.close()