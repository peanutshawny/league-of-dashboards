import mysql.connector
from db_creds import host, user, passwd, database

# connecting to database
db = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database
)

lol_cursor = db.cursor()

# creating empty tables
lol_cursor.execute('CREATE TABLE IF NOT EXISTS League ('
                   'ID INT NOT NULL,'
                   'Region VARCHAR(255),'
                   'PRIMARY KEY (ID));'
                   )

lol_cursor.execute('CREATE TABLE IF NOT EXISTS Summoner ('
                   'ID VARCHAR(255) NOT NULL,'
                   'LeagueID INT DEFAULT NULL,'
                   'Name VARCHAR(255),'
                   'Level INT,'
                   'PRIMARY KEY (ID),'
                   'FOREIGN KEY (LeagueID) REFERENCES League(ID));'
                   )

lol_cursor.execute('CREATE TABLE IF NOT EXISTS Game ('
                   'ID BIGINT NOT NULL,'
                   'Duration INT,'
                   'Timestamp BIGINT,'
                   'PRIMARY KEY (ID));'
                   )

lol_cursor.execute('CREATE TABLE IF NOT EXISTS Item ('
                   'ID INT NOT NULL,'
                   'Name VARCHAR(255),'
                   'Gold INT,'
                   'Tier INT,'
                   'PRIMARY KEY (ID));'
                   )

lol_cursor.execute('CREATE TABLE IF NOT EXISTS Champion ('
                   'ID INT NOT NULL,'
                   'Name VARCHAR(255),'
                   'Attack INT,'
                   'Defense INT,'
                   'Difficulty INT,'
                   'Magic INT,'
                   'HealthHegenPerLevel FLOAT,'
                   'AttackDamagePerLevel FLOAT,'
                   'HealthRegen FLOAT,'
                   'CriticalStrikeChancePerLevel FLOAT,'
                   'ArmorPerLevel FLOAT,'
                   'HealthPerLevel FLOAT,'
                   'Armor FLOAT,'
                   'Mana FLOAT,'
                   'AttackRange FLOAT,'
                   'ManaPerLevel FLOAT,'
                   'MoveSpeed FLOAT,'
                   'CriticalStrikeChance FLOAT,'
                   'AttackDamage FLOAT,'
                   'ManaRegenPerLevel FLOAT,'
                   'AttackSpeed FLOAT,'
                   'ManaRegen FLOAT,'
                   'Health FLOAT,'
                   'MagicResist FLOAT,'
                   'PercentAttackSpeedPerLevel FLOAT,'
                   'MagicResistPerLevel FLOAT,'
                   'PRIMARY KEY (ID));'
                   )

lol_cursor.execute('CREATE TABLE IF NOT EXISTS Item_pick ('
                   'SummonerID VARCHAR(255) DEFAULT NULL,'
                   'Item0 INT DEFAULT NULL,'
                   'Item1 INT DEFAULT NULL,'
                   'Item2 INT DEFAULT NULL,'
                   'Item3 INT DEFAULT NULL,'
                   'Item4 INT DEFAULT NULL,'
                   'Item5 INT DEFAULT NULL,'
                   'Item6 INT DEFAULT NULL,'
                   'FOREIGN KEY (SummonerID) REFERENCES Summoner(ID),'
                   'FOREIGN KEY (Item0) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item1) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item2) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item3) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item4) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item5) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item6) REFERENCES Item(ID));'
                   )

lol_cursor.execute('CREATE TABLE IF NOT EXISTS Game_item ('
                   'GameID BIGINT NOT NULL,'
                   'Item0 INT DEFAULT NULL,'
                   'Item1 INT DEFAULT NULL,'
                   'Item2 INT DEFAULT NULL,'
                   'Item3 INT DEFAULT NULL,'
                   'Item4 INT DEFAULT NULL,'
                   'Item5 INT DEFAULT NULL,'
                   'Item6 INT DEFAULT NULL,'
                   'FOREIGN KEY (GameID) REFERENCES Game(ID),'
                   'FOREIGN KEY (Item0) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item1) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item2) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item3) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item4) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item5) REFERENCES Item(ID),'
                   'FOREIGN KEY (Item6) REFERENCES Item(ID));'
                   )

lol_cursor.execute('CREATE TABLE IF NOT EXISTS Champ_select ('
                   'SummonerID VARCHAR(255) DEFAULT NULL,'
                   'ChampionID INT NOT NULL,'
                   'FOREIGN KEY (ChampionID) REFERENCES Champion(ID),'
                   'FOREIGN KEY (SummonerID) REFERENCES Summoner(ID));'
                   )

lol_cursor.execute('CREATE TABLE IF NOT EXISTS Game_champ ('
                   'GameID BIGINT NOT NULL,'
                   'ChampionID INT NOT NULL,'
                   'FOREIGN KEY (GameID) REFERENCES Game(ID),'
                   'FOREIGN KEY (ChampionID) REFERENCES Champion(ID));'
                   )

lol_cursor.execute('CREATE TABLE IF NOT EXISTS Game_instance ('
                   'ID INT NOT NULL,'
                   'GameID BIGINT NOT NULL,'
                   'SummonerID VARCHAR(255) DEFAULT NULL,'
                   'Win BOOL,'
                   'Kills INT,'
                   'Deaths INT,'
                   'Assists INT,'
                   'DoubleKills INT,'
                   'TripleKills INT,'
                   'QuadraKills INT,'
                   'PentaKills INT,'
                   'TotalDamageDealtToChampions INT,'
                   'DamageDealtToObjectives INT,'
                   'VisionScore INT,'
                   'TimeCCingOthers INT,'
                   'TotalDamageTaken INT,'
                   'GoldEarned INT,'
                   'WardsPlaced INT,'
                   'FOREIGN KEY (GameID) REFERENCES Game(ID),'
                   'FOREIGN KEY (SummonerID) REFERENCES Summoner(ID));'
                   )

db.close()
