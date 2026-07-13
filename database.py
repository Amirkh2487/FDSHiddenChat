import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS messages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender INTEGER,
    receiver INTEGER,
    message_id INTEGER
)
""")

conn.commit()


def add_user(user_id):
    cur.execute("INSERT OR IGNORE INTO users(user_id) VALUES(?)", (user_id,))
    conn.commit()


def save_message(sender, receiver, message_id):
    cur.execute(
        "INSERT INTO messages(sender,receiver,message_id) VALUES(?,?,?)",
        (sender, receiver, message_id),
    )
    conn.commit()


def get_messages(user_id):
    cur.execute(
        "SELECT sender,message_id FROM messages WHERE receiver=?",
        (user_id,),
    )
    return cur.fetchall()
