# in store_in_sqlite.py

def purge(periode = 365):

    sql = """\
DELETE
FROM items
WHERE last_seen <= DATE((SELECT MAX(last_seen) FROM items), '-? days');"""

    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(sql, (periode, ))
    conn.commit()
    conn.close()

# in main_purge_db.py

from src.persistence.store_in_sqlite import purge

if __name__ == '__main__':
    purge()