from SimpleGet import simple_get
from bs4 import BeautifulSoup

baseUrl = 'http://www.vegasinsider.com'

def get_team_lines(teamUrl):
    raw = simple_get(teamUrl)
    html = BeautifulSoup(raw, 'html.parser')
    print(teamUrl)

def get_vegas_lines():
    vegasLines = []
    teamsPageUrl = baseUrl + '/nba/teams/'
    raw = simple_get(teamsPageUrl)
    html = BeautifulSoup(raw, 'html.parser')
    table = html.select('table')[7]
    for td in table.tbody.select('td'):
        if td.a is not None and td.a.get('href'):
            teamUrl = baseUrl + td.a.get('href')
            teamLines = get_team_lines(teamUrl)
            vegasLines.extend(teamLines)
    return None

get_vegas_lines()
