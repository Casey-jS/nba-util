from nba_api.stats.endpoints import playergamelogs


def get_game_logs(playerID):
    

    lst = []

    for i in range(5):
        game = playergamelogs.PlayerGameLogs(season_nullable='2022-23', player_id_nullable=playerID).get_dict()["resultSets"][0]["rowSet"][i]
        game_dict = {
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
        lst.append(game_dict)
    return lst


print(get_game_logs(2544))