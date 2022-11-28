import sqlite3
import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

player_set = leaguedashplayerstats.LeagueDashPlayerStats().get_dict()["resultSets"][0]["rowSet"]

# keys = leaguedashplayerstats.LeagueDashPlayerStats().get_dict()["resultSets"][0]["headers"]

""" i = 0

for key in keys:
    print(str(i) + ": " + key)
    i += 1 """

def get_stat(id, stat_str):

    statDict = {
        "TEAM" : 3,
        "AGE" : 4,
        "GP" : 5,
        "FGPCT" : 12,
        "FG3PCT" : 15,
        "PTS" : 30,
        "AST" : 23,
        "REB" : 22,
        "BLK" : 26,
        "STL" : 25,
    }   

    stat_index = statDict[stat_str]

    rstat = 0
    total_rstat = 0
    for player_info in player_set:
        if player_info[0] == id:
            total_rstat = player_info[stat_index] # get stat from data structure
            games_played = player_info[6]          # divide it by games played to get the average
            rstat = total_rstat / games_played
            break
    if "." not in str(rstat):
        str_stat = str(rstat)
        str_stat += ".0"
        rstat = float(str_stat)
    return rstat
def create_stat_db():
    db = sqlite3.connect("player_stats.db")

    with open("player_stats.sql") as f:
        db.executescript(f.read())

    db.row_factory = sqlite3.Row

    for player_stats in player_set:
        id = player_stats[0]
        name = player_stats[1]
        ppg = round(get_stat(id, "PTS"), 1)
        apg = round(get_stat(id, "AST"), 1)
        rpg = round(get_stat(id, "REB"), 1)
        spg = round(get_stat(id, "STL"), 1)
        bpg = round(get_stat(id, "BLK"), 1)
        team = player_stats[4]
        gp = player_stats[6]
        fgpct = player_stats[13] * 100
        fg3pct = player_stats[16] * 100
        ftpct = player_stats[19] * 100
        age = player_stats[5]

        insert_string = "INSERT INTO PlayerStats (id, fullName, team, games, age, ppg, apg, rpg, spg, bpg, fgpct, fg3pct, ftpct) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db.execute(insert_string, (id, name, team, gp, age, ppg, apg, rpg, spg, bpg, fgpct, fg3pct, ftpct))
        db.commit()
    db.close()


# create_stat_db()

def get_db():
    db = sqlite3.connect("player_stats.db")
    db.row_factory = sqlite3.Row
    return db

def test_get_stats(name):
    db = get_db()

    stats = db.execute("SELECT * FROM PlayerStats WHERE fullName = ?", (name,)).fetchone()

    format = ["ID: ", "Name: ", "TEAM: ", "GP: ", "AGE: ", "PPG: ", "APG: ", "RPG: ", "SPG: ", "BPG: ", "FG%: ", "3P%: ", "FT%: "]

    for i in range(13):
        print(format[i] + str(stats[i]))

test_get_stats("Luke Kennard")







