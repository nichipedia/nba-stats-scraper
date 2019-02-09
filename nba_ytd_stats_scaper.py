from SimpleGet import simple_get
from bs4 import BeautifulSoup

baseUrl = 'https://www.basketball-reference.com'

def parse_team_page(teamUrl):
    raw = simple_get(teamUrl)
    html = BeautifulSoup(raw, 'html.parser')
    table = html.find('table')
    currentYear = baseUrl + table.tbody.select('tr')[0].th.a.get('href')
    get_team_game_log(currentYear)

def get_team_game_log(teamUrl):
    raw = simple_get(teamUrl)
    html = BeautifulSoup(raw, 'html.parser')
    bottom_nav = html.find('div', {'id': 'bottom_nav_container'})
    game_log_page = baseUrl + bottom_nav.select('li')[3].a.get('href')
    get_team_stats(game_log_page)

def get_team_stats(teamUrl):
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
            print(dateStats)
            ytdStats.append(dateStats)



# Main Loop Below
teamsUrl = baseUrl + '/teams/'
raw = simple_get(teamsUrl)
html = BeautifulSoup(raw, 'html.parser')
table = html.find('table', {'id': 'teams_active'})
for tr in table.tbody.select('tr'):
    if tr.th.get('class') is not None:
        #print(tr.th['class'])
        if tr.th['class'][0] == 'left':
            teamUrl = baseUrl + tr.th.a.get('href')
            parse_team_page(teamUrl)
