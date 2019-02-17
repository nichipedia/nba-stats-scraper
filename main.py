from nba_ytd_stats_scraper import get_nba_ytd_stats 

nbaStats = get_nba_ytd_stats()


print(nbaStats[64])

def insertMuliRow(rows):
    command = 'INSERT INTO NBA_GAME_STATS () VALUES ()'



#con = sqlite3.connect('app.db')

#cur = con.cursor()

#cur.execute('INSERT INTO stuff(NAME,AGE) VALUES ("blarg", 21)')
#
#con.commit()


