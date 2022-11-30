import sqlite3

def create_users_db():
    db = sqlite3.connect("databases/users.db")

    with open("databases/users.sql") as f:
        db.executescript(f.read())

    db.commit()
    db.close()
# create_users_db()
