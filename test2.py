from nba_api.stats.endpoints import leaguegamelog

""" keys = leaguegamelog.LeagueGameLog(counter = 1).get_dict()['resultSets'][0]['headers']

i = 0
for key in keys:
    print(str(i) + ": " + key)
    i += 1  """

 
game = leaguegamelog.LeagueGameLog(counter = 5,
                                   direction = "DESC",
                                   player_or_team_abbreviation = "P",
                                   sorter = "DATE").get_dict()['resultSets'][0]['rowSet'][0]

i = 0
for stat in game:
    print(str(i) + ": " + str(stat))







