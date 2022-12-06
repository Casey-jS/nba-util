from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams
import db_util
import sqlite3
import time
import random

i = 0


""" keys = teamgamelog.TeamGameLog(team_id = 1610612740).get_dict()['resultSets'][0]['headers']
for key in keys:
    print(str(i) + ": " + str(key))
    i += 1 """






def insert_team_logs(db, teamID):

    

    games = teamgamelog.TeamGameLog(team_id = teamID, date_from_nullable = "11/10/22", date_to_nullable="12/04/2022").get_dict()['resultSets'][0]['rowSet']
    insert_string = "INSERT INTO TeamLogs (teamID, opp, res, pts, ast, reb, fg, fg3, ft, tov, stl, blk) VALUES (?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?)"
    i = 0
    for game in games:
        if i == 5:
            break
        fgm = game[9]
        fga = game[10]
        fg3m = game[12]
        fg3a = game[13]
        ftm = game[15]
        fta = game[16]

        opp = game[3][-3:]
        print("Date: " + str(game[2]))
        res = game[4]
        pts = game[26]
        ast = game[21]
        reb = game[20]
        fg = str(fgm) + "/" + str(fga)
        fg3 = str(fg3m) + "/" + str(fg3a)
        ft = str(ftm) + "/" + str(fta)
        tov = game[24]
        stl = game[22]
        blk = game[23]

        time_to_sleep = round(random.uniform(.7, 1.8), 2)
        time.sleep(time_to_sleep)

        db.execute(insert_string, (teamID, opp, res, pts, ast, reb, fg, fg3, ft, tov, stl, blk))
        i += 1


    db.commit()
 

def create_teamlogs():

    db = sqlite3.connect('databases/team_logs.db')
    db.row_factory = sqlite3.Row

    with open('databases/team_logs.sql') as f:
        db.executescript(f.read())

    with open('teamIDs.txt', 'r') as f:
        ids = f.readlines()

        for id in ids:
            teamID = int(id)
            insert_team_logs(db, teamID)
        
    db.close()

create_teamlogs()

     


