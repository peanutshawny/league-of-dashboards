# lol-player-dashboard
Applying data modeling in MySQL to build an ETL pipeline from the Riot API, resulting in a database that can be used as a means of improving one's own gameplay. The database is then connected to a Dash app where queries from the database can be visualized in an interative way.

## Creating the database
Because I couldn't find a way to pull a list of random summoner IDs, I found a list of summoner IDs online posted by Riot that tries to solve this exact issue. Next, I extracted a list of around 30,000 matches that includes these summoner IDs. I then pulled a list of all in-game items and champions. To completely fill out my data model, I created intersecting entities from matches, champions, items, and summoners.

Finally, I wrote scripts to create an empty mysql database and load the aforementioned tables into it.

## Creating the dashboard

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
