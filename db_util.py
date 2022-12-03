import sqlite3
import json

def get_db(database):
    db = sqlite3.connect("databases/" + database + ".db")
    db.row_factory = sqlite3.Row
    return db




def get_id(name):
    db = get_db("player_stats")
    cursor = db.cursor()
    query = "SELECT * FROM PlayerStats WHERE fullName = ?"
    id = cursor.execute(query, (name,)).fetchone()

    cursor.close()
    return id[0]

def dict_from_row(row):
    return dict(zip(row.keys(), row))

def get_league_leaders(stat) -> list[dict]:
    db = get_db("player_stats")
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
    db = get_db("team_stats")
    cursor = db.cursor()
    query = "SELECT * FROM TeamStats ORDER BY wrank asc"
    teams = cursor.execute(query).fetchall()
    cursor.close()
    lst = []
    for team in teams:
        team_dict = dict_from_row(team)
        lst.append(team_dict)
    return lst

def get_roster(teamID):
    db = get_db("player_stats")
    cursor = db.cursor()
    query = "SELECT * FROM PlayerStats WHERE teamID = ? ORDER BY fantasyRank asc"
    roster = cursor.execute(query, (teamID,)).fetchall()
    cursor.close()
    lst = []
    for player in roster:
        roster_dict = dict_from_row(player)
        lst.append(roster_dict)

    return lst

def get_player_by_id(id):
    db = get_db("player_stats")
    cursor = db.cursor()
    player = cursor.execute("SELECT * FROM PlayerStats WHERE id = ?", (id,)).fetchone()
    db.close()
    player_dict = dict_from_row(player)
    return player_dict

def connect_users():
    db = sqlite3.connect("databases/users.db")
    db.row_factory = sqlite3.Row
    return db
def user_exists(username):
    db = connect_users()
    cursor = db.cursor()

    user = cursor.execute("SELECT 1 FROM Users WHERE userName = ?", (username,))
    if user.fetchone():
        return True
    return False



def validate_user(username, password):
    db = connect_users()
    cursor = db.cursor()
    user = cursor.execute("SELECT 1 FROM Users WHERE userName = ? AND password = ?", (username, password))
    if user.fetchone():
        return True
    return False
    

def get_data_json(data):
    return json.dumps(data)

def get_new_id():
    db = connect_users()
    cursor = db.cursor()

    maxID = cursor.execute("SELECT 1 id FROM Users order by id desc").fetchone()
    return maxID[0] + 1


print(get_new_id())





    



