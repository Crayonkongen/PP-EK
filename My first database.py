import sqlite3

from pathlib import Path

conn = sqlite3.connect("test.db")
database_path = Path.cwd().joinpath("test.db")
conn = sqlite3.connect(database_path)
c = conn.cursor()

query = '''CREATE TABLE IF NOT EXISTS user(
student_id INTEGER PRIMARY KEY NOT NULL,
first_name TEXT NOT NULL,
grade INTEGER
)
'''
c.execute(query)

try:
   c.execute("INSERT INTO user (student_id, first_name, grade) VALUES (?, ?, ?)", (1, 'Alex', 2))
except sqlite3.IntegrityError as e:
   print(f"[Error]: {e}")

try:
   c.execute("INSERT INTO user (student_id, first_name, grade) VALUES (?, ?, ?)", (2, 'Rubin', 0))
except sqlite3.IntegrityError as e:
   print(f"[Error]: {e}")

try:
   c.execute("INSERT INTO user (student_id, first_name, grade) VALUES (?, ?, ?)", (3, 'Protein', 12))
except sqlite3.IntegrityError as e:
   print(f"[Error]: {e}")

finally:
   conn.commit()
   conn.close()