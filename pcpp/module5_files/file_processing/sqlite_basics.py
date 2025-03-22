import sqlite3

conn = sqlite3.connect('tasks.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')

c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('my first task', 1))

tasks = [
    ('my second task', 2),
    ('my third task', 3),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)

for row in c.execute('SELECT * FROM tasks'):
    print(row)

c.execute('SELECT * FROM tasks')
rows = c.fetchall()
for row in rows:
    print(row)

c.execute('SELECT * FROM tasks')
row = c.fetchone()

print(row)

conn.commit()
conn.close()

