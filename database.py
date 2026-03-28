import sqlite3

conn = sqlite3.connect("health.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    chat_id INTEGER PRIMARY KEY,
    sleep REAL,
    water REAL,
    steps INTEGER,
    mood INTEGER,
    last_score INTEGER
)
""")
conn.commit()


def save_user(chat_id, data, score):
    cursor.execute("""
    INSERT OR REPLACE INTO users (chat_id, sleep, water, steps, mood, last_score)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (chat_id, data["sleep"], data["water"], data["steps"], data["mood"], score))
    conn.commit()


def get_all_users():
    cursor.execute("SELECT chat_id FROM users")
    return cursor.fetchall()