SELECT
	c.name AS champion,
    CASE WHEN gi.Win = 1 THEN 'Win' ELSE 'Lose' END AS winloss
FROM game_instance gi
	INNER JOIN champ_select cs ON gi.SummonerID = cs.SummonerID
	INNER JOIN game_champ gc ON gi.GameID = gc.GameID AND gc.ChampionID = cs.ChampionID
    INNER JOIN champion c on gc.ChampionID = c.ID
