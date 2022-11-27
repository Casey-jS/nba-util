
stat_map = {
    "PTS" : 2,
    "AST" : 3,
    "REB" : 4,
    "STL" : 5,
    "BLK" : 6
}

def get_stat(stat, playerID):
    # player is a 
    player = db.get_player(playerID)

    stat_index = stat_map[stat]

    return float(player[stat_index])







    






    