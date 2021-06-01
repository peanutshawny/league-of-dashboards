import mysql.connector
from db_creds import host, user, passwd, database

import pandas as pd

# connecting to database
db = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database
)

# calculating champion winrates
winrate_df = pd.read_sql('''
SELECT DISTINCT
	c.name AS champion,
    sum(gi.Win)/count(gi.Win) AS winrate
FROM game_instance gi
	INNER JOIN champ_select cs ON gi.SummonerID = cs.SummonerID
	INNER JOIN game_champ gc ON gi.GameID = gc.GameID AND gc.ChampionID = cs.ChampionID
    INNER JOIN champion c on gc.ChampionID = c.ID
GROUP BY
	c.name
''', con=db)

# calculating champion pickrates
pickrate_df = pd.read_sql('''
SELECT DISTINCT
	c.name AS champion,
    (COUNT(ChampionID) OVER (PARTITION BY ChampionID))/(SELECT COUNT(*) FROM game) * 100 AS pickrate
FROM game_champ gc
	INNER JOIN champion c ON gc.ChampionID = c.Id
''', con=db)

# calculating damage dealt per champion --

print(pickrate_df)
