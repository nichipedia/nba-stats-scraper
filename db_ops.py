import sqlite3

def insertMuliRowStats(games):
    rowsTuple = []
    for row in games:
        rowsTuple.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25]))
    con = sqlite3.connect('app.db')
    cur = con.cursor()
    command = 'INSERT INTO NBA_GAME_STATS(TEAM_NAME, GAME_TOTAL, WIN_PCT, GAME_NUMBER, GAME_DATE, HOME_FLAG, OPP_NAME, WON_FLAG, TEAM_POINTS, OPP_POINTS, TEAM_FG, TEAM_FG_ATTEMPTS, FG_PCT, TEAM_3P, TEAM_3P_ATTEMPTS, TEAM_3P_PCT, TEAM_FT, TEAM_FT_ATTEMPTS, TEAM_FT_PCT, TEAM_REBOUNDS, GAME_REBOUNDS, TEAM_ASSISTS, TEAM_STEALS, TEAM_BLOCKS, TEAM_TURNOVERS, TEAM_FOULS) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
    cur.executemany(command, rowsTuple)
    con.commit()
    con.close()

def insertMultiRowLines(lines):
    rowsTuple = []
    for row in lines:
        rowsTuple.append((row[0], row[1], row[2], row[3], row[4]))
    con = sqlite3.connect('app.db')
    cur = con.cursor()
    command = 'INSERT INTO NBA_GAME_LINES(LINE_DATE, TEAM_NAME, OPP_NAME, SPREAD, GAME_LINE) VALUES(?, ?, ?, ?, ?);'
    cur.executemany(command, rowsTuple)
    con.commit()
    con.close()