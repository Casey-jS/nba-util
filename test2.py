from nba_api.stats.endpoints import leaguestandingsv3
from nba_api.stats.static import players

standings = leaguestandingsv3.LeagueStandingsV3(season='2022-23').get_dict()['resultSets'][0]['headers']

i = 0
for key in standings:
    print(str(i) + ": " + key)
    i += 1 





