# lol-player-dashboard
Applying data modeling in MySQL to build an ETL pipeline from the Riot API, resulting in a database that can be used as a means of improving one's own gameplay. The database is then connected to a Dash app where queries from the database can be visualized in an interative way

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
