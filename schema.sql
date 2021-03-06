CREATE TABLE NBA_GAME_STATS(ID INTEGER PRIMARY KEY AUTOINCREMENT, TEAM_NAME VARCHAR(3) NOT NULL, GAME_TOTAL VARCHAR(3) NOT NULL, 
WIN_PCT VARCHAR(5) NOT NULL, GAME_NUMBER VARCHAR(3) NOT NULL, GAME_DATE INTEGER NOT NULL, HOME_FLAG VARCHAR(1) NOT NULL,
OPP_NAME VARCHAR(3) NOT NULL, WON_FLAG VARCHAR(1) NOT NULL, TEAM_POINTS VARCHAR(3) NOT NULL, OPP_POINTS VARCHAR(3) NOT NULL,
TEAM_FG VARCHAR(3) NOT NULL, TEAM_FG_ATTEMPTS VARCHAR(3) NOT NULL, FG_PCT VARCHAR(5) NOT NULL, TEAM_3P VARCHAR(3) NOT NULL,
TEAM_3P_ATTEMPTS VARCHAR(3) NOT NULL, TEAM_3P_PCT VARCHAR(5) NOT NULL, TEAM_FT VARCHAR(3) NOT NULL, TEAM_FT_ATTEMPTS VARCHAR(3) NOT NULL,
TEAM_FT_PCT VARCHAR(5) NOT NULL, TEAM_REBOUNDS VARCHAR(3) NOT NULL, GAME_REBOUNDS VARCHAR(3) NOT NULL, TEAM_ASSISTS VARCHAR(3) NOT NULL,
TEAM_STEALS VARCHAR(3) NOT NULL, TEAM_BLOCKS VARCHAR(3) NOT NULL, TEAM_TURNOVERS VARCHAR(3) NOT NULL, TEAM_FOULS VARCHAR(3) NOT NULL);

CREATE TABLE NBA_GAME_LINES(ID INTEGER PRIMARY KEY AUTOINCREMENT, LINE_DATE INTEGER NOT NULL, TEAM_NAME VARCHAR(3) NOT NULL, OPP_NAME VARCHAR(3) NOT NULL, 
SPREAD VARCHAR(3) NOT NULL, GAME_LINE VARCHAR(5) NOT NULL);

INSERT INTO NBA_GAME_STATS(TEAM_NAME, GAME_TOTAL, WIN_PCT, GAME_NUMBER, GAME_DATE, HOME_FLAG, OPP_NAME, WON_FLAG, TEAM_POINTS, OPP_POINTS, TEAM_FG, TEAM_FG_ATTEMPTS,
FG_PCT, TEAM_3P, TEAM_3P_ATTEMPTS, TEAM_3P_PCT, TEAM_FT, TEAM_FT_ATTEMPTS, TEAM_FT_PCT, TEAM_REBOUNDS, GAME_REBOUNDS, TEAM_ASSISTS, TEAM_STEALS, TEAM_BLOCKS
TEAM_TURNOVERS, TEAM_FOULS) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

INSERT INTO NBA_GAME_LINES(LINE_DATE, TEAM_NAME, OPP_NAME, SPREAD, GAME_LINE) VALUES(?, ?, ?, ?, ?);