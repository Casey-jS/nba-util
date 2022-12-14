import sqlite3
from nba_api.stats.endpoints import leaguedashteamstats


def create_team_db():
    db = sqlite3.connect("databases/team_stats.db")
    with open("databases/team_stats.sql") as f:
        db.executescript(f.read())
    db.row_factory = sqlite3.Row

    for team in team_set:
        id = team[0]
        name = team[1]
        wins = team[3] 
        losses = team[4]
        win_pct = round(team[5], 3) * 100 # to format into a pct
        ppg = round(team[12], 3) * 100 # to format into a pct
        plusminus = team[27]
        three_pct = round((team[26] / (wins + losses)), 2)
        rank = team[29]

        insert_string = "INSERT INTO TeamStats (id, teamName, wins, losses, wpct, ppg, fg3pct, plusminus, wrank) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db.execute(insert_string, (id, name, wins, losses, win_pct, three_pct, ppg, plusminus, rank))
        db.commit()

team_set = leaguedashteamstats.LeagueDashTeamStats().get_dict()["resultSets"][0]['rowSet']

""" i = 0
for key in team_set:
    print(str(i) + ": " + key)
    i += 1 """




def get_team_stat(teamID, stat):
    statDict = {
        "W" : 3,
        "L" : 4,
        "W_PCT" : 5,
        "PTS" : 26,
        "FG3_PCT" : 12,
        "PLUS_MINUS" : 27,
        "W_RANK" : 29
    }

    stat_index = statDict[stat]

    rstat = 0

    for team in team_set:
        if team[0] == teamID:
            rstat = team[stat_index]
            break
    return rstat



def get_db():
    db = sqlite3.connect("databases/team_stats.db")
    db.row_factory = sqlite3.Row
    return db

def test_get_stats(team_name):
    db = get_db()

    stats = db.execute("SELECT * FROM TeamStats WHERE teamName = ?", (team_name,)).fetchone()

    format = ["ID: ", "Name: ", "W: ", "L: ", "W%: ", "PPG: ", "3%: ", "+/-: ", "RANK: "]

    for i in range(9):
        print(format[i] + str(stats[i]))



#create_team_db()

test_get_stats("Boston Celtics")