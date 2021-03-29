# lol-player-database
Applying data modeling in MySQL to build an ETL pipeline from the Riot API, resulting in a database that can be used as a means of improving one's own gameplay.  

## Riot API extract
I first extracted match, champion, player, and item data from the Riot API with the list of summoner IDs.

## Sample queries

```sql
SELECT

  game_instance.Win,
  champion.Name
  
FROM game_instance

  INNER JOIN game_champ ON game_instance.GameID = game_champ.GameID
  INNER JOIN champion ON game_champ.ChampionID = champion.ID
  
WHERE champion.name = "Ashe"
```
