SELECT
game_instance.Win,
champion.Name
FROM game_instance
INNER JOIN game_champ ON game_instance.GameID = game_champ.GameID
INNER JOIN champion ON game_champ.ChampionID = champion.ID
WHERE champion.name = "Ashe"