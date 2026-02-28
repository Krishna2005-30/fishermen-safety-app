import sqlite3
import os

db_path = os.path.join(os.getcwd(), 'data.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()

# ------------------------
# Harbors Table
# ------------------------
c.execute('''
CREATE TABLE IF NOT EXISTS harbors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
)
''')

sample_harbors = [
    ('Kochi Harbor', 9.9312, 76.2673),
    ('Alappuzha Harbor', 9.4981, 76.3388),
    ('Kollam Harbor', 8.8932, 76.6141)
]

c.execute('SELECT COUNT(*) FROM harbors')
if c.fetchone()[0] == 0:
    c.executemany('INSERT INTO harbors (name, latitude, longitude) VALUES (?, ?, ?)', sample_harbors)

# ------------------------
# Fish Hotspots Table
# ------------------------
c.execute('''
CREATE TABLE IF NOT EXISTS fish_hotspots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
)
''')

sample_fish = [
    ('Fish Zone 1', 9.9400, 76.2500),
    ('Fish Zone 2', 9.5100, 76.3500),
    ('Fish Zone 3', 8.9000, 76.6200)
]

c.execute('SELECT COUNT(*) FROM fish_hotspots')
if c.fetchone()[0] == 0:
    c.executemany('INSERT INTO fish_hotspots (name, latitude, longitude) VALUES (?, ?, ?)', sample_fish)

conn.commit()
conn.close()

print("Database created successfully!")