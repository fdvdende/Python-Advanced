# importing sqlite3 module
import sqlite3

# create conn by using object
# to connect with hotel_data database
conn = sqlite3.connect('hotel_data.db')

# query to create a table named FOOD1
conn.execute("DROP TABLE IF EXISTS food")
conn.execute("""\
CREATE TABLE food
(ID          INT PRIMARY KEY NOT NULL,
 NAME		 TEXT NOT NULL,
 COST		 INT NOT NULL,
 WEIGHT	     INT);""")

# insert query to insert food details in
# the above table
conn.execute("INSERT INTO food VALUES (1, 'cakes', 800, 10 )")
conn.execute("INSERT INTO food VALUES (2, 'biscuits', 100, 20 )")
conn.execute("INSERT INTO food VALUES (3, 'chocos', 1000, 30 )")

print("All data in food table:")

# create a cursor object for select query
cursor = conn.execute("SELECT * FROM food")

# display all data from hotel table
for row in cursor:
    print(row)

conn.close()
