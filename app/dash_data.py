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
    sum(gi.Win)/count(gi.Win) AS winrate,
    1 - sum(gi.Win)/count(gi.Win) AS loserate
FROM game_instance gi
	INNER JOIN champ_select cs ON gi.SummonerID = cs.SummonerID
	INNER JOIN game_champ gc ON gi.GameID = gc.GameID AND gc.ChampionID = cs.ChampionID
    INNER JOIN champion c on gc.ChampionID = c.ID
GROUP BY
	c.name
''', con=db).set_index('champion')

# calculating champion pickrates
pickrate_df = pd.read_sql('''
SELECT DISTINCT
	c.name AS champion,
    (COUNT(ChampionID) OVER (PARTITION BY ChampionID))/(SELECT COUNT(*) FROM game) AS pickrate,
    1 - (COUNT(ChampionID) OVER (PARTITION BY ChampionID))/(SELECT COUNT(*) FROM game) AS nopickrate
FROM game_champ gc
	INNER JOIN champion c ON gc.ChampionID = c.Id
''', con=db).set_index('champion')

# calculating average damage dealt per champion
damage_df = pd.read_sql('''
SELECT DISTINCT
	c.name AS champion,
	avg(gi.TotalDamageDealtToChampions) as avg_damage_per_game
FROM game_instance gi
	INNER JOIN champ_select cs ON gi.SummonerID = cs.SummonerID
	INNER JOIN game_champ gc ON gi.GameID = gc.GameID AND gc.ChampionID = cs.ChampionID
    INNER JOIN champion c on gc.ChampionID = c.ID
GROUP BY
	c.name
ORDER BY
	avg_damage_per_game
''', con=db)

# transposing in preparation for pie chart
winrate_df = winrate_df.T
pickrate_df = pickrate_df.T
