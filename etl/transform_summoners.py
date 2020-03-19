# importing packages
import pandas as pd

# reading match list
import json

# importing functions and other dfs
from etl_functions import id_match
from transform_matches import item_picks_df

path = 'D:/Python/lol_dashboard'
with open(path + '/data/loaded_summoners.json') as f:
    summoner_list = json.load(f)

# populating the summoner table
summoner_ids = []
summoner_name = []
summoner_level = []

for summoner in summoner_list:
    try:
        summoner_ids.append(summoner['id'])
        summoner_name.append(summoner['name'])
        summoner_level.append(summoner['summonerLevel'])
    except:
        continue

# transforming into dataframes 
summoner_dict = {'ID': summoner_ids, 'name': summoner_name, 'level': summoner_level}

summoner_df = pd.DataFrame(summoner_dict)

# creating fake league id
summoner_df['leagueID'] = 1

# adding missing IDs to parent entities to not break FK constraints
summoner_df = id_match(summoner_df, 'ID', item_picks_df, ['summonerID'])