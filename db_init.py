import sqlite3
from nba_api.stats.static import players

players_dict = players.get_active_players()
db = sqlite3.connect("players.db")

with open("players.sql") as f:
    db.executescript(f.read())

cursor = db.cursor()
db.row_factory = sqlite3.Row

def get_db():
    db = sqlite3.connect("bugs.db")
    db.row_factory = sqlite3.Row
    return db

# occupy database with updated player info
for player in players_dict:
    fname = player['first_name']
    lname = player['last_name']
    id = int(player['id'])

    insert_string = "INSERT INTO Players (id, fname, lname) VALUES (?, ?, ?)"
    db.execute(insert_string, (id, fname, lname))
    db.commit()

cursor.close()



