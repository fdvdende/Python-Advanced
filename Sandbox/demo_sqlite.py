import sqlite3

connection = sqlite3.connect('database.sqlite')

# drop_query = 'DROP TABLE IF EXISTS users;'
create_query = 'CREATE TABLE IF NOT EXISTS users ( \
                id INTEGER PRIMARY KEY, \
                name VARCHAR(80), \
                hash VARCHAR(1024));'

# connection.execute(drop_query)
connection.execute(create_query)
connection.commit()

data = [('Peter',  'sdshdjfksfdhkfh'),
        ('Aljoscha',  'sqwwqwqtyhkfh')]

insert_query = 'INSERT INTO users (name, hash) VALUES (?, ?)'

connection.executemany(insert_query, data)
connection.commit()

select_query = 'SELECT * FROM users'

result = connection.execute(select_query)
for record in result.fetchall():
    print(record)
