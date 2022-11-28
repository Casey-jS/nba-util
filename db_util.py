import sqlite3
import json

def get_db():
    db = sqlite3.connect("databases/player_stats.db")
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

def dict_from_row(row):
    return dict(zip(row.keys(), row))

def get_league_leaders(stat) -> list[dict]:
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM PlayerStats ORDER BY " + stat + " desc LIMIT 30"
    top30 = cursor.execute(query).fetchall()
    cursor.close()
    db.close()

    lst = []
    for player in top30:
        player_dict = dict_from_row(player)
        lst.append(player_dict)
    
    return lst

def get_teams():
    db = sqlite3.connect("databases/team_stats.db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    query = "SELECT * FROM TeamStats ORDER BY wrank asc"
    teams = cursor.execute(query).fetchall()
    cursor.close()
    lst = []
    for team in teams:
        team_dict = dict_from_row(team)
        lst.append(team_dict)
    return lst


def get_data_json(data):
    return json.dumps(data)








    



