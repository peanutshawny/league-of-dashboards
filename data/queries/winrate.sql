SELECT DISTINCT
	c.name AS champion,
    sum(gi.Win)/count(gi.Win) AS winrate
FROM game_instance gi
	INNER JOIN champ_select cs ON gi.SummonerID = cs.SummonerID
	INNER JOIN game_champ gc ON gi.GameID = gc.GameID AND gc.ChampionID = cs.ChampionID
    INNER JOIN champion c on gc.ChampionID = c.ID
GROUP BY
	c.name