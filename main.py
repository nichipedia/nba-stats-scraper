from nba_ytd_stats_scraper import get_nba_ytd_stats 

nbaStats = get_nba_ytd_stats()

homePoints = int(nbaStats[0][7])
oppPoints = int(nbaStats[0][8])
gameTotal = (homePoints + oppPoints)
print(gameTotal)
print(nbaStats[0])
