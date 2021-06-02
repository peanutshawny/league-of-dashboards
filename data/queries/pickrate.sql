SELECT DISTINCT
	c.name AS champion,
    (COUNT(ChampionID) OVER (PARTITION BY ChampionID))/(SELECT COUNT(*) FROM game) AS pickrate
FROM game_champ gc
	INNER JOIN champion c ON gc.ChampionID = c.Id