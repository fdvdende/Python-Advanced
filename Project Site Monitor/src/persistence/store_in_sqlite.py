import os
import sqlite3

dirname = 'data'
filename = 'items.db'

dbname = os.path.join(dirname, filename)


def store(summary):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = f"""\
INSERT INTO items (name, url, title, link, date, first_seen, last_seen, status, html)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""

    for item in summary:
        c.execute(sql, (item['name'],
                        item['url'],
                        item['title'],
                        item['link'],
                        item['date'],
                        item['first_seen'],
                        item['last_seen'],
                        item['status'],
                        item['html']))

    conn.commit()
    conn.close()


def update_or_insert(summary):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    for item in summary:

        sql = """\
            SELECT name FROM items 
            WHERE name = ? AND title = ?;"""

        c.execute(sql, (item['name'], item['title']))
        row = c.fetchone()
        if row is None:

            sql = f"""\
                INSERT INTO items (name, url, title, link, date, first_seen, last_seen, status, html)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""

            c.execute(sql, (item['name'],
                            item['url'],
                            item['title'],
                            item['link'],
                            item['date'],
                            item['first_seen'],
                            item['last_seen'],
                            item['status'],
                            item['html']))

            conn.commit()

        else:

            sql = f"""\
                UPDATE items SET last_seen = ?
                WHERE name = ? AND title = ?;"""

            c.execute(sql, (item['last_seen'], item['name'], item['title']))

            conn.commit()

    conn.close()



def load():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    sql = """\
SELECT name, url, title, link, date, first_seen, last_seen, status, html 
FROM items 
ORDER BY id DESC;"""

    results = []
    for row in c.execute(sql):
        results.append({
            'name': row[0],
            'url': row[1],
            'title': row[2],
            'link': row[3],
            'date': row[4],
            'first_seen': row[5],
            'last_seen': row[6],
            'status': row[7],
            'html': row[8]
        })

    conn.close()

    return results


def create_database():
    sql = """\
CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT, 
    url TEXT, 
    title TEXT, 
    link TEXT, 
    date TEXT, 
    first_seen TEXT, 
    last_seen TEXT,
    status TEXT,
    html TEXT)"""

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def update_status(title, status):

    sql = """\
    UPDATE items
    SET status = ?
    WHERE title = ?;"""

    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(sql, (status, title))
    conn.commit()
    conn.close()


def purge(periode = 365):

    sql = """\
DELETE
FROM items
WHERE last_seen <= DATE((SELECT MAX(last_seen) FROM items), ?);"""

    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(sql, (f'-{periode} days', ))
    conn.commit()
    conn.close()


