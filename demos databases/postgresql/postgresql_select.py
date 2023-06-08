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
    cur.execute("SELECT * FROM Products")

    while True:
        row = cur.fetchone()

        if row == None:
            break

        print("Product: " + row[1] + "\t\tPrice: " + str(row[2]))

except psycopg2.DatabaseError as e:
    if conn:
        conn.rollback()

    print('Error %s' % e)
    sys.exit(1)

finally:
    if conn:
        conn.close()