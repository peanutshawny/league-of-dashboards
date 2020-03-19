# importing packages
import pandas as pd

# using requests and cassiopeia python wrapper pull data from riot api
import cassiopeia as cass

# reading match list
import json

# importing functions
from etl_functions import id_match

path = 'D:/Python/lol_dashboard'
with open(path + '/data/loaded_matches.json') as f:
    match_list = json.load(f)

# setting api key
key = 'RGAPI-83d9b69d-993f-48df-8bf6-0573100e4db0'
cass.set_riot_api_key(key)

# pulling items, and champion data
items = cass.get_items(region='NA')
items = list(items)

champs = cass.get_champions(region='NA')
champs = list(champs)

# filling out the match, summoner, match instance, champion selection 
# this essentially populates all intersecting entities
match_ids = []
match_ids_intersect = []
duration = []
creation = []
summoner_ids = []
champ_ids_intersect = []
summoner_stats = []

# iterate over all matches, populate match entity
for match in match_list:

    try:
        match_ids.append(match['gameId'])
        duration.append(match['gameDuration'])
        creation.append(match['gameCreation'])

        # game instance, item picks, and game items entities
        for i in range(len(match['participantIdentities'])):
            match_ids_intersect.append(match['gameId'])
            summoner_ids.append(match['participantIdentities'][i]['player']['summonerId'])
            summoner_stats.append(match['participants'][i]['stats'])

        # champ select and game champions entities
        for i in range(len(match['participants'])):
            champ_ids_intersect.append(match['participants'][i]['championId'])

    except:
        continue

# list of distinct summoner ids
summoner_ids_distinct = list(set(summoner_ids))

# writing to later extract summoner data
with open(path + '/data/summoners.json', 'w') as w:
    json.dump(summoner_ids_distinct, w)

# appending all useful champion data
champ_ids = []
champ_names = []
champ_info = []
champ_stats = []
champ_tags = []

for champ in champs:
    champ_ids.append(champ.id)
    champ_names.append(champ.name)
    champ_info.append(champ.info.to_dict())
    champ_stats.append(champ.stats.to_dict())
    champ_tags.append(champ.tags)

# appending all useful items data
item_ids = []
item_names = []
item_gold = []
item_tiers = []

for item in items:
    item_ids.append(item.id)
    item_names.append(item.name)
    item_gold.append(item.gold.total)
    item_tiers.append(item.tier)

# transforming all lists into dataframe
# champions
champ_dict = {'ID': champ_ids, 'name': champ_names, 'info': champ_info, 'stats': champ_stats, 'tags': champ_tags}

# items
items_dict = {'ID': item_ids, 'name': item_names, 'gold': item_gold, 'tier': item_tiers}

# item picks
item_picks_dict = {'summonerID': summoner_ids, 'stats': summoner_stats}

# matches
matches_dict = {'ID': match_ids, 'duration': duration, 'timestamp': creation}

# match items
match_items_dict = {'gameID': match_ids_intersect, 'stats': summoner_stats}

# match instance
match_instance_dict = {'summonerID': summoner_ids, 'gameID': match_ids_intersect, 'stats': summoner_stats}

# champ select
champ_select_dict = {'summonerID': summoner_ids, 'championID': champ_ids_intersect}

# match champs
game_champs_dict = {'gameID': match_ids_intersect, 'championID': champ_ids_intersect}

# transforming into dataframes 
champ_df = pd.DataFrame(champ_dict)
items_df = pd.DataFrame(items_dict)
matches_df = pd.DataFrame(matches_dict)

item_picks_df = pd.DataFrame(item_picks_dict)
match_items_df = pd.DataFrame(match_items_dict)
match_instance_df = pd.DataFrame(match_instance_dict)
champ_select_df = pd.DataFrame(champ_select_dict)
game_champs_df = pd.DataFrame(game_champs_dict)

# splitting dictionaries within columns into separate columns
champ_df = champ_df.join(champ_df['info'].apply(pd.Series))
champ_df = champ_df.join(champ_df['stats'].apply(pd.Series))

# splitting dicts within the dataframes
item_picks_df = item_picks_df.join(item_picks_df['stats'].apply(pd.Series))
match_items_df = match_items_df.join(match_items_df['stats'].apply(pd.Series))
match_instance_df = match_instance_df.join(match_instance_df['stats'].apply(pd.Series))

# filtering on only the key columns
item_picks_df = item_picks_df[['summonerID', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6']]
match_items_df = match_items_df[['gameID', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6']]
match_instance_df = match_instance_df[['gameID', 'summonerID', 'win', 'kills', 'deaths',
                                       'assists', 'doubleKills', 'tripleKills', 'quadraKills', 'pentaKills',
                                       'totalDamageDealtToChampions', 'damageDealtToObjectives', 'visionScore',
                                       'timeCCingOthers', 'totalDamageTaken', 'goldEarned', 'wardsPlaced']]

champ_df.drop(['info', 'stats', 'tags'], axis=1, inplace=True)

# adding missing IDs to parent entities to not break FK constraints
items_df = id_match(items_df, 'ID', item_picks_df, ['item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6'])