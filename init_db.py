import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS uploads (
        id INTEGER PRIMARY KEY,
        filename TEXT NOT NULL,       
        upload_time TEXT NOT NULL
        )
""")

conn.commit()
conn.close()

print("Database initialized.")