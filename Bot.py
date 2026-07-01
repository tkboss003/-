import sqlite3

db = sqlite3.connect("data/bot.db")

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
name TEXT
)
""")

db.commit()
