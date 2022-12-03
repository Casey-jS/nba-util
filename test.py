import sqlite3

def get_db():
    db = sqlite3.connect('databases/game_logs.db')
    db.row_factory = sqlite3.Row
    return db

def dict_from_row(row):
    return dict(zip(row.keys(), row))



def get_last5_for_player(playerID):
    db = get_db()
    cursor = db.cursor()
    logs = cursor.execute("SELECT * FROM GameLog WHERE playerID = ?", (playerID,)).fetchall()
    lst = []
    cursor.close()
    for game in logs:
        game_dict = dict_from_row(game)
        print(game_dict)
        lst.append(game_dict)

    return lst


lebron_games = get_last5_for_player(203500)
print(lebron_games)



