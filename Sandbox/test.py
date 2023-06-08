s = """\
    CREATE TABLE todo(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        note TEXT,
        deadline TEXT,
        prioriteit TEXT,
        status TEXT,
        active BOOL)"""

print(repr(s))

from textwrap import dedent
print(repr(dedent(s)))
