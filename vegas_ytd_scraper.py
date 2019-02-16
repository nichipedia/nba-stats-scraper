from SimpleGet import simple_get
from bs4 import BeautifulSoup
import datetime

baseUrl = 'http://www.vegasinsider.com'

def get_team_lines(teamUrl, teamName):
    raw = simple_get(teamUrl)
    teamLines = []
    html = BeautifulSoup(raw, 'html.parser')
    table = html.select('table')[4]
    lastGameText = table.tbody.select('td')[0].text
    lastGameDate = extract_last_game_date(lastGameText)
   
    table = html.select('table')[12]
    for tr in table.tbody.select('tr'):
        if (tr.select('a') is not None and 'Date' not in tr.select('td')[0].text.strip()):
            line = []
            try:
                date = create_correct_date(tr.select('td')[0].text.strip())
                line.append(date)
                line.append(teamName)
                line.append(tr.select('td')[1].a.text)
                line.append(tr.select('td')[2].text)
                line.append(tr.select('td')[3].text)
                teamLines.append(line)
                if (tr.select('td')[0].text.strip() == lastGameDate):
                    return teamLines
            except IndexError:
                print(tr)
            except AttributeError:
                print(tr)
    print(teamLines)

def create_correct_date(gameDate):
    now = datetime.datetime.now()
    year = int(now.year)
    month = int(now.month)
    if (month > 9):
        newDate = gameDate.strip() + ' ' + str(year)
        return datetime.datetime.strptime(newDate, '%b %d %Y').date().isoformat()
    else:
        if 'Dec' in gameDate or 'Nov' in gameDate or 'Oct' in gameDate:
            newDate = gameDate.strip() + ' ' + str(year-1)
            return datetime.datetime.strptime(newDate, '%b %d %Y').date().isoformat()
        else:
            newDate = gameDate.strip() + ' ' + str(year)
            return datetime.datetime.strptime(newDate, '%b %d %Y').date().isoformat()


def extract_last_game_date(lastGameText):
    new = lstrip_word(lastGameText, 'LAST GAME - ')
    try:
        date = datetime.datetime.strptime(new, '%A %b. %d, %Y').date()
        dateFormated = date.strftime("%b %d").lstrip("0").replace(" 0", " ")
        return dateFormated
    except ValueError:
        print(lastGameText)
        print(new)
   
def lstrip_word(string, word):
    if string.startswith(word):
        return string[len(word):]
    return string


def get_vegas_lines():
    vegasLines = []
    teamsPageUrl = baseUrl + '/nba/teams/'
    raw = simple_get(teamsPageUrl)
    html = BeautifulSoup(raw, 'html.parser')
    table = html.select('table')[7]
    for td in table.tbody.select('td'):
        if td.a is not None and td.a.get('href'):
            teamUrl = baseUrl + td.a.get('href')
            teamName = td.a.text
            teamLines = get_team_lines(teamUrl, teamName)
            vegasLines.extend(teamLines)
    return vegasLines

get_vegas_lines()
