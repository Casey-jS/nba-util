from nba_api.stats.endpoints import playergamelogs
from nba_api.stats.static import players
import sqlite3

def create_gamelogs_db():
    db = sqlite3.connect("databases/game_logs.db")

    with open("databases/game_log.sql") as f:
        db.executescript(f.read())

    db.row_factory = sqlite3.Row

    all_game_logs = get_game_logs()

    insert_string = "INSERT INTO GameLogs (playerID, opp, wl, minPlayed, fg, threes, reb, ast, stl, blk, fpts) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    
    for game in all_game_logs:
        db.execute(insert_string, (game['id'], game['opp'], game['wl'], game['min'], game['fg'], game['3p'], game['reb'], game['ast'], game['stl'], game['blk'], game['fpts']))
        db.commit()

    db.close()

def get_game_logs():
    
    players_list = players.get_active_players()
    lst = []

    for i in range(len(players_list)):
        player_id = players_list[i]['id']
        for j in range(5):
            game = get_game_log_for_player(player_id, j)
            lst.append(game)
    return lst

def get_game_log_for_player(playerID, game_number) -> dict:

    game = playergamelogs.PlayerGameLogs(season_nullable='2022-23', player_id_nullable=playerID).get_dict()["resultSets"][0]["rowSet"][game_number]
    game_dict = {
        "id" : game[1],
        "opp" : game[9].split(' ')[2],
        "wl" : game[10],
        "min": game[11],
        "fg" : str(game[12]) + "/" + str(game[13]),
        "3p" : str(game[15]) + "/" + str(game[16]),
        "reb" : game[23],
        "ast" : game[24],
        "stl" : game[26],
        "blk" : game[27],
        "fpts" : game[33]
    }

    return game_dict


create_gamelogs_db()