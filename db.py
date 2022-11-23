import sqlite3

def get_db():
    db = sqlite3.connect("players.db")
    db.row_factory = sqlite3.Row
    return db

def get_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("Select * from Players")
    row_count = len(cursor.fetchall())
    print(row_count)
    cursor.close()
    return row_count
    
def get_player(id):
    db = get_db()
    player = db.execute("SELECT * FROM Players WHERE id = ?", (id,)).fetchone()
    db.close()
    return player

def get_id(fname, lname):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM Players WHERE lname = ?"
    ids = cursor.execute(query, (lname,)).fetchall()

    if len(ids) == 1:
        cursor.close()
        db.close()
        return ids[0][0]

    query += "AND fname = ?"

    id = cursor.execute(query, (lname, fname)).fetchone()
    cursor.close()
    return id[0]

    



