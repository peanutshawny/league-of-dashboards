SELECT DISTINCT
	c.name AS champion,
    (COUNT(ChampionID) OVER (PARTITION BY ChampionID))/(SELECT COUNT(*) FROM game) AS pickrate,
    1 - (COUNT(ChampionID) OVER (PARTITION BY ChampionID))/(SELECT COUNT(*) FROM game) AS nopickrate
FROM game_champ gc
	INNER JOIN champion c ON gc.ChampionID = c.Id