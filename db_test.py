import sqlite3

def get_db():
    db = sqlite3.connect("players.db")
    db.row_factory = sqlite3.Row
    return db

def test(lname):
    db = get_db()
    player = db.execute("SELECT * FROM Players WHERE lname = ?", (lname,)).fetchone()
    db.close()
    print(player[2])

def get_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("Select * from Players")
    row_count = len(cursor.fetchall())
    print(row_count)
    cursor.close()

get_count()

