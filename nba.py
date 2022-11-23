from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo as common

players_dict = players.get_active_players()

def get_player(name):

    player_df = [player for player in players_dict if player['full_name']== name][0]
    return player_df


player = get_player("Damian Lillard")
print(player["last_name"])


    