import sqlite3
import json

def get_db(database):
    db = sqlite3.connect("databases/" + database + ".db")
    db.row_factory = sqlite3.Row
    return db

def get_list_of_dicts(rows):
    lst = []
    for row in rows:
        d = dict_from_row(row)
        lst.append(d)
    return lst

def dict_from_row(row):
    return dict(zip(row.keys(), row))

def get_league_leaders(stat):
    db = get_db("player_stats")
    cursor = db.cursor()
    query = "SELECT * FROM PlayerStats ORDER BY " + stat + " desc LIMIT 30"
    top30 = cursor.execute(query).fetchall()
    lst = get_list_of_dicts(top30)

    return lst

def get_teams():
    db = get_db("team_stats")
    cursor = db.cursor()
    query = "SELECT * FROM TeamStats ORDER BY wrank asc"
    teams = cursor.execute(query).fetchall()
    cursor.close()
    lst = get_list_of_dicts(teams)
    return lst

def get_roster(teamID):
    db = get_db("player_stats")
    cursor = db.cursor()
    query = "SELECT * FROM PlayerStats WHERE teamID = ? ORDER BY fantasyRank asc"
    roster = cursor.execute(query, (teamID,)).fetchall()
    cursor.close()
    lst = get_list_of_dicts(roster)
    return lst

def get_team_info(teamID):
    db = get_db("team_stats")
    cursor = db.cursor()
    info = cursor.execute("select teamName, wrank, wins, losses from TeamStats where id = ?", (teamID,)).fetchone()
    return dict_from_row(info)



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
    print("Checking if user " + username + " exists")
    cursor.execute("SELECT count(*) FROM Users WHERE userName = ?", (username,))
    data = cursor.fetchone()[0]
    if data == 0:
        print("User " + username + " does not exist")
        return False
    print("User exists")
    return True



def validate_user(username, password):
    db = connect_users()
    cursor = db.cursor()
    user = cursor.execute("SELECT 1 FROM Users WHERE userName = ? AND password = ?", (username, password))
    if user.fetchone():
        return True
    return False
    

def get_data_json(data):
    return json.dumps(data)

def get_new_id() -> int:
    db = connect_users()
    cursor = db.cursor()

    maxID = cursor.execute("SELECT 1 id FROM Users order by id desc").fetchone()

    if len(maxID) == 0:
        return 

    return maxID[0] + 1

def new_fav_player(user, player):
    db = sqlite3.connect('databases/fav_players.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("INSERT INTO FavPlayers (userName, playerID) VALUES (?, ?)", (user, player))
    db.commit()
    db.close()

def get_fav_players(userName):
    print("Getting favorite players for user "+ userName)
    db = get_db("fav_players")
    cursor = db.cursor()
    players = cursor.execute("SELECT * FROM FavPlayers WHERE userName = ?", (userName,)).fetchall()

    if len(players) == 0:
        return False
    lst = []
    for player in players:
        player_id = dict_from_row(player)['playerID']
        lst.append(player_id)

    stats = []
    for id in lst:
        playerStats = get_stats_for_player(id)
        stats.append(playerStats)


    return stats

def get_stats_for_player(playerID):
    db = get_db("player_stats")
    cursor = db.cursor()
    stats = cursor.execute("SELECT * FROM PlayerStats WHERE id = ?", (playerID,)).fetchone()
    stat_dict = dict_from_row(stats)

    cursor.close()
    db.close()

    return stat_dict

def new_user(usr, pswd):

    db = get_db("users")

    cursor = db.cursor()
    new_id = get_new_id()
    cursor.execute("INSERT INTO Users (id, userName, password) VALUES (?, ?, ?)", (new_id, usr, pswd))


def get_teamID_by_name(name: str) -> int:
    db = get_db("team_stats")
    cursor = db.cursor()
    id = cursor.execute("SELECT id FROM TeamStats WHERE teamName = ?", (name,)).fetchone()[0]
    return id


def get_team_log(teamID):
    db = get_db("team_logs")
    cursor = db.cursor()
    games = cursor.execute("SELECT * FROM TeamLogs WHERE teamID = ?", (teamID,)).fetchall()
    return get_list_of_dicts(games)


def get_standings(conference):
    db = sqlite3.connect('databases/standings.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    standings = cursor.execute("SELECT * FROM Standings WHERE conf = ? ORDER BY lrank LIMIT 10", (conference,)).fetchall()
    return get_list_of_dicts(standings)



def get_top4_stat(stat):
    db = get_db("player_stats")
    cursor = db.cursor()
    top4 = cursor.execute("SELECT id, fullName, " + stat + " FROM PlayerStats ORDER BY " + stat + " DESC LIMIT 4").fetchall()
    return get_list_of_dicts(top4)

def is_favorited(userName, playerID):
    db = get_db("fav_players")
    cursor = db.cursor()
    exists = cursor.execute("SELECT * FROM FavPlayers WHERE userName = ? and playerID = ?", (userName, playerID))

    if exists.fetchone():
        return True
    return False

def get_search_results(text):
    db = get_db("player_stats")
    cursor = db.cursor()
    top5 = cursor.execute("SELECT id, fullName FROM PlayerStats WHERE fullName like '%" + text + "%' ORDER BY ppg DESC LIMIT 5").fetchall()
    return get_list_of_dicts(top5)

def get_top_bets():
    db = get_db("bets")
    cursor = db.cursor()
    top5 = cursor.execute("SELECT * from Bets LIMIT 5").fetchall()
    return get_list_of_dicts(top5)

def new_bet(user, player, playerID, amount, stat, opp):
    db = get_db("bets")
    insert_string = "INSERT INTO Bets (user, playerID, playerName, stat, amount, opp) VALUES (?, ?, ?, ?, ?, ?)"
    db.execute(insert_string, (user, playerID, player, stat, float(amount), opp))
    db.commit()
    db.close()

def get_bets(user):
    db = get_db("bets")
    cursor = db.cursor()
    bets = cursor.execute("SELECT * FROM Bets WHERE user = ?", (user,)).fetchall()

    return get_list_of_dicts(bets)