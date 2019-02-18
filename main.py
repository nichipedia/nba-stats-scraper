from nba_ytd_stats_scraper import get_nba_ytd_stats 
from vegas_ytd_scraper import get_vegas_lines
from db_ops import insertMuliRowStats
from db_ops import insertMultiRowLines
import sqlite3

dbloc = ''

#nbaStats = get_nba_ytd_stats()
nbaLines = get_vegas_lines()


#insertMuliRowStats(nbaStats)
insertMultiRowLines(nbaLines)







#cur.execute('INSERT INTO stuff(NAME,AGE) VALUES ("blarg", 21)')
#
#con.commit()


