import pandas as pd
import sqlite3

conn = sqlite3.connect('population.db')

with conn:
    conn.execute("DROP TABLE IF EXISTS Population")
    conn.execute("CREATE TABLE Population(id INTEGER PRIMARY KEY, country TEXT, population INT)")
    conn.execute("INSERT INTO Population VALUES(NULL,'Germany',81197537)")
    conn.execute("INSERT INTO Population VALUES(NULL,'France', 66415161)")
    conn.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")
    conn.execute("INSERT INTO Population VALUES(NULL,'Italy', 60795612)")
    conn.execute("INSERT INTO Population VALUES(NULL,'Spain', 46439864)")

    sql = "SELECT country FROM Population WHERE population > 50000000;"
    df = pd.read_sql_query(sql, conn)

for country in df['country']:
    print(country)
