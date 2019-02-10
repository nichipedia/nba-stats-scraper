from SimpleGet import simple_get
from bs4 import BeautifulSoup
from nba_ytd_stats_scraper import get_nba_ytd_stats 
import datetime

def get_daily_stats():
    """
    Returns a list of todays current game stats!
    """
    now = datetime.date.today()
    todaysGames = []
    nbaStats = get_nba_ytd_stats()
    for game in nbaStats:
        if game[4] == '2019-02-09':
            todaysGames.append(game)
    return todaysGames

today = get_daily_stats()
print(today)
