import pickle
import sqlite3
import random

from typing import List, Dict

class Ranking:
    """Documentation"""

    def __init__(self):
        self.initialize_sqlite()

        self._ranking = self.load()

    def add_score(self, name: str, duration: int, score: (float, int)):
        self._ranking.append({'name': name,
                              'duration': duration,
                              'score': score})

    def load(self):
        filename = '../data/ranking.pickle'
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except:
            return []

    def store(self):
        filename = '../data/ranking.pickle'
        with open(filename, 'wb') as f:
            return pickle.dump(self._ranking, f)

    def top_ten(self) -> List[Dict]:
        return sorted(self._ranking,
                      key = lambda item: (item['score'], -item['duration']),
                      reverse = True)[:10]


    def initialize_sqlite(self):

        sql = """\
CREATE TABLE IF NOT EXISTS ranking
(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT,
    score INT,
    duration FLOAT
);"""

        conn = sqlite3.connect('ranking.db')
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        conn.close()

    def append_to_sqlite(self, ranking):
        sql = "INSERT INTO ranking (name, score, duration) VALUES (?, ?, ?);"

        conn = sqlite3.connect('ranking.db')
        c = conn.cursor()
        c.execute(sql, (ranking['name'], ranking['score'], ranking['duration']))
        conn.commit()
        conn.close()

    def load_from_sqlite(self, where_clause = None):
        sql = "SELECT name, score, duration FROM ranking;"

        if where_clause:
            sql = sql.rstrip(';') + '\nWHERE ' + where_clause + ';'

        conn = sqlite3.connect('ranking.db')
        c = conn.cursor()
        rankings = list(c.execute(sql))
        conn.commit()
        conn.close()

        return rankings

    def top_ten_from_sqlite(self) -> List[Dict]:
        sql = """\
SELECT name, score, duration 
FROM ranking
ORDER BY score DESC, duration ASC
LIMIT 10;"""

        conn = sqlite3.connect('ranking.db')
        c = conn.cursor()
        rankings = list(c.execute(sql))
        conn.commit()
        conn.close()

        return rankings


# ------------------

if __name__ == '__main__':

    ranking = Ranking()

    # ranking.append_to_sqlite({'name': f'Peter', 'duration': random.randint(10, 30), 'score': random.choice([10, 30, 60, 100, 150])})

    # for i in range(20):
    #     ranking.append_to_sqlite({'name': f'Player{i}', 'duration': random.randint(10, 30), 'score': random.choice([10, 30, 60, 100, 150])})

    for ranking_tuple in ranking.load_from_sqlite():
        print(ranking_tuple)

    print('Top Ten')
    for i, ranking_tuple in enumerate(ranking.top_ten_from_sqlite(), start = 1):
        print(i, ranking_tuple)


    # ranking = Ranking()
    # ranking.add_score('Peter', 30, 10)
    # ranking.store()
    # for quiz in ranking.top_ten():
    #     print(quiz)