import sqlite3
import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

player_set = leaguedashplayerstats.LeagueDashPlayerStats().get_dict()["resultSets"][0]["rowSet"]

def get_stat(id, stat_str):

    statDict = {
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
    
    return rstat
def create_stat_db():
    db = sqlite3.connect("player_stats.db")

    with open("player_stats.sql") as f:
        db.executescript(f.read())

    db.row_factory = sqlite3.Row

    for player_stats in player_set:
        id = player_stats[0]
        name = player_stats[1]
        ppg = round(get_stat(id, "PTS"), 2)
        apg = round(get_stat(id, "AST"), 2)
        rpg = round(get_stat(id, "REB"), 2)
        spg = round(get_stat(id, "STL"), 2)
        bpg = round(get_stat(id, "BLK"), 2)

        insert_string = "INSERT INTO PlayerStats (id, fullName, ppg, apg, rpg, spg, bpg) VALUES (?, ?, ?, ?, ?, ?, ?)"
        db.execute(insert_string, (id, name, ppg, apg, rpg, spg, bpg))
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

    format = ["ID: ", "Name: ", "PPG: ", "APG: ", "RPG: ", "SPG: ", "BPG: "]

    for i in range(6):
        print(format[i] + str(stats[i]))


test_get_stats("Shai Gilgeous-Alexander")






