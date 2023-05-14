import sqlite3

db = sqlite3.connect("src/leaderboard.db")
db.isolation_level = None
db.execute("CREATE TABLE Players (id INTEGER PRIMARY KEY, name TEXT, score REAL)")
db.execute("INSERT INTO Players (name, score) VALUES ('PENA', 85.4)")
db.execute("INSERT INTO Players (name, score) VALUES ('SAMU', 71.9)")
db.execute("INSERT INTO Players (name, score) VALUES ('EMMI', 59.7)")
