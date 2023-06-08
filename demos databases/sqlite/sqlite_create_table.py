# Python3 program to demonstrate SQLite3 datatypes
# and corresponding Python3 types

# import the sqlite3 package
import sqlite3

# create connection to database
conn = sqlite3.connect('companies.db')
conn.row_factory = sqlite3.Row

# Create a exam_hall relation
conn.execute("DROP TABLE IF EXISTS exam_hall")
conn.execute("""CREATE TABLE exam_hall(
NAME TEXT,
PIN INTEGER,
OCCUPANCY REAL,
LOGO BLOB);""")

# Open the logo file in read, binary mode
# read the image as binary data into a variable
with open('../content/logo apple.png', 'rb') as f:
	img = f.read()

# Insert tuples for the relation
conn.execute("""INSERT INTO exam_hall VALUES(
'Apple',1125,98.6,?)""", (img,))
conn.execute("""INSERT INTO exam_hall VALUES(
NULL,1158,80.5,?)""", (img,))

# Query the data, print the data and its type
# note: Printing the image binary data is impractical due to its huge size
# instead number of bytes are being printed using len()
cursor = conn.execute("""SELECT * FROM exam_hall;""")
for row in cursor.fetchall():
	d = dict(row)
	d['LOGO'] = len(row['LOGO'])
	print(d)

	print([type(row[k]) for k in d.keys()])

conn.close()
