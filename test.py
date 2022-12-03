from nba_api.stats.static import players


players_list = players.get_active_players()

print(players_list)