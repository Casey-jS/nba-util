from nba_api.stats.endpoints import leaguestandings
import time
import random
import sqlite3

def create_standings():

    db = sqlite3.connect('databases/standings.db')
    db.row_factory = sqlite3.Row

    with open('databases/standings.sql') as f:
        db.executescript(f.read())

    standings = leaguestandings.LeagueStandings().get_dict()['resultSets'][0]['rowSet']
    print(len(standings))
    insert_string = "INSERT INTO Standings (teamID, teamName, conf, lrank, record, home, away, last10) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    for team in standings:
        teamID = team[2] # not shown
        teamName = team[4]
        conf = team[5]  # not shown
        lrank = team[15] # not shown
        record = team[16]
        home = team[17]
        away = team[18]
        last10 = team[19]

        print("Finished inserting " + teamName + " records")

        db.execute(insert_string, (teamID, teamName, conf, lrank, record, home, away, last10))
    db.commit()
    db.close()


create_standings()

db = sqlite3.connect('databases/standings.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()

ids = cursor.execute("SELECT teamID FROM Standings").fetchall()

for id in ids:
    print(id[0])
