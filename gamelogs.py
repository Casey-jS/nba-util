from nba_api.stats.endpoints import playergamelogs
from nba_api.stats.static import players
import sqlite3
import time


headers =  {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        }

def get_last5(id):
    lst = []
    for i in range(5):

        

        
        log = playergamelogs.PlayerGameLogs(player_id_nullable=2544, headers = headers, timeout=100).get_dict()['resultSets'][0]['rowSet'][i]
        print("got a game log")
        game_dict = {
            "result" : log[5],
            "opp" : log[4][-3:],
            "pts" : log[24],
            "fg" : str(log[7]) + "/" + str(log[8]),
            "fg3" : str(log[10]) + "/" + str(log[11]),
            "reb" : log[18],
            "ast" : log[19],
            "stl" : log[20],
            "blk" : log[21]
        }
        lst.append(game_dict)

        time.sleep(.6)

    return lst

"""
playerID int not null,
opp text not null,
wl text not null,
fg text not null,
threes text not null,
reb int not null,
ast int not null,
stl int not null,
blk int not null
"""

def create_logs_db():
    
    db = sqlite3.connect('databases/game_logs.db')
    with open('databases/game_logs.sql') as f:
        db.executescript(f.read())

    insert_string = "INSERT INTO GameLogs (playerID, opp, wl, pts, fg, threes, reb, ast, stl, blk) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    with open('active_ids.txt', 'r') as fp:
        id = fp.readline()
        while id:
            last5 = get_last5(int(id))
            for game in last5:
                res = game["result"]
                opp = game['opp']
                pts = game['pts']
                fg = game['fg']
                fg3 = game['fg3']
                reb = game['reb']
                ast = game['ast']
                stl = game['stl']
                blk = game['blk']

                db.execute(insert_string, (int(id), opp, res, pts, fg, fg3, reb, ast, stl, blk))
    db.commit()
    db.close()

# create_logs_db()

def get_active_ids():
    db = sqlite3.connect('databases/player_stats.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    ids = cursor.execute("SELECT ID FROM PlayerStats WHERE games > 4").fetchall()

    for id in ids:
        print(id[0])

def view_db():
    db = sqlite3.connect('databases/game_logs.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    count = cursor.execute("SELECT COUNT(*) playerID from GameLogs").fetchone()[0]
    print(count)

# view_db()

print(get_last5(2544))












