import sqlite3

def create_favs_db():
    db = sqlite3.connect('databases/fav_players.db')

    with open('databases/fav_players.sql') as f:
        db.executescript(f.read())

    db.row_factory = sqlite3.Row

    insert_string = "INSERT INTO FavPlayers (userName, playerID) VALUES (?, ?)"
    db.execute(insert_string, ("admin", 2544))
    db.commit()
    db.close()

create_favs_db()