from SimpleGet import simple_get
from bs4 import BeautifulSoup
import time
import datetime
from TEAMS import TEAMS

baseUrl = 'https://www.basketball-reference.com'

def extract_current_year_team_page(teamUrl):
    """
    Returns the url to the teams most current year.
    Expects a url to the teams history page on basketball-reference.com
    """
    raw = simple_get(teamUrl)
    html = BeautifulSoup(raw, 'html.parser')
    table = html.find('table')
    currentYear = baseUrl + table.tbody.select('tr')[0].th.a.get('href')
    return currentYear
    #get_team_game_log(currentYear)

def extract_team_game_log_url(teamUrl):
    """
    Returns the url to the teams gamelog [age on basketball-reference.com.
    Expects a url to the teams main page for most current year.
    """
    raw = simple_get(teamUrl)
    html = BeautifulSoup(raw, 'html.parser')
    bottom_nav = html.find('div', {'id': 'bottom_nav_container'})
    game_log_page = baseUrl + bottom_nav.select('li')[3].a.get('href')
    return game_log_page
    #get_team_stats(game_log_page)

# TODO: Make this either optionally return a df or a list
def get_team_stats(teamUrl):
    """
    Returns a DataFrame, OR List of Lists of a single teams year to date game stats.
    Expects to have the url to the teams gamelog page on basketball-reference.com.
    """
    ytdStats = []
    raw = simple_get(teamUrl)
    html = BeautifulSoup(raw, 'html.parser')
    table = html.find('table', {'id': 'tgl_basic'})
    for tr in table.tbody.select('tr'):
        if tr.get('id') is not None:
            #Need to load this into either a dictionary OR a dataframe OR list!
            dateStats = []
            for td in tr.select('td'):
                dateStats.append(td.text)
            ytdStats.append(dateStats)
    return ytdStats

# TODO: Add a varible to specify list of dataframe
def get_nba_ytd_stats():
    """
    Return a list or dataframe of the NBA's year to date game data extracted from Basketball-Reference.com!
    """
    nbaStats = []
    teamsUrl = baseUrl + '/teams/'
    raw = simple_get(teamsUrl)
    html = BeautifulSoup(raw, 'html.parser')
    table = html.find('table', {'id': 'teams_active'})
    for tr in table.tbody.select('tr'):
        if tr.th.get('class') is not None:
            #print(tr.th['class'])
            if tr.th['class'][0] == 'left':
                teamUrl = baseUrl + tr.th.a.get('href')
                teamName = tr.th.a.text
                currentYear = extract_current_year_team_page(teamUrl)
                gameLogUrl = extract_team_game_log_url(currentYear)
                teamStats = get_team_stats(gameLogUrl)
                totalGames = 0.0
                wins = 0.0
                for game in teamStats:
                    totalGames = totalGames + 1
                    if game[4] == 'W':
                        wins = wins + 1
                    pct = '{0:.3g}'.format(wins/totalGames)
                    teamPoints = int(game[5])
                    oppPoints = int(game[6])
                    totalPoints = teamPoints + oppPoints
                    if (game[2] == '@'):
                        game[2] = 'A'
                    else:
                        game[2] = 'H'
                    game[1] = time.mktime(datetime.datetime.strptime(game[1], '%Y-%m-%d').timetuple())
                    game.insert(0, str(pct))
                    game.insert(0, str(totalPoints))
                    game.insert(0, TEAMS[teamName])
                nbaStats.extend(teamStats)
    return nbaStats