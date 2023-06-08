#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

conn = None
try:
    connection_string = "host='localhost' " \
                        "port='5432' " \
                        "dbname='postgres' " \
                        "user='postgres' " \
                        "password='postgres'"
    conn = psycopg2.connect(connection_string)
    conn.autocommit = True

    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS Products;")
    cur.execute("CREATE DATABASE Products;")
    cur.execute("CREATE TABLE Products(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    cur.execute("INSERT INTO Products VALUES(1,'Milk',5)")
    cur.execute("INSERT INTO Products VALUES(2,'Sugar',7)")
    cur.execute("INSERT INTO Products VALUES(3,'Coffee',3)")
    cur.execute("INSERT INTO Products VALUES(4,'Bread',5)")
    cur.execute("INSERT INTO Products VALUES(5,'Oranges',3)")

except psycopg2.DatabaseError as e:
    print('Error %s' % e)

    if conn:
        conn.rollback()

    sys.exit(1)

finally:
    if conn:
        conn.close()