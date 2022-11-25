import sqlite3
import json


column_names = [
    "id",
    "fullName",
    "ppg",
    "apg",
    "rpg",
    "spg",
    "bpg"
]

def get_db():
    db = sqlite3.connect("player_stats.db")
    db.row_factory = sqlite3.Row
    return db

def get_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("Select * from PlayerStats")
    row_count = len(cursor.fetchall())
    print(row_count)
    cursor.close()
    return row_count

def get_player(id):
    db = get_db()
    player = db.execute("SELECT * FROM PlayerStats WHERE id = ?", (id,)).fetchone()
    db.close()
    return player

def get_id(name):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM PlayerStats WHERE fullName = ?"
    id = cursor.execute(query, (name,)).fetchone()

    cursor.close()
    return id[0]

# maybe add capability to filter by position
# string passed in should be column name
def get_league_leaders(stat) -> list[dict]:
    db = get_db()
    cursor = db.cursor()
    players = []
    query = "SELECT * FROM PlayerStats ORDER BY " + stat + " desc LIMIT 10"
    top10 = cursor.execute(query).fetchall()
    cursor.close()
    db.close()

    lst = []
    for player in top10:
        player_dict = dict_from_row(player)
        lst.append(player_dict)
    
    return lst

def dict_from_row(row):
    return dict(zip(row.keys(), row))


def get_data_json(data):
    return json.dumps(data)








    


