# importing sqlalchemy
from sqlalchemy import create_engine

# importing dataframes
from transform_matches import champ_df, items_df, matches_df, item_picks_df, match_items_df, \
    match_instance_df, champ_select_df, game_champs_df
from transform_summoners import summoner_df

# mapping dataframes in the correct order for iteration
frames = {'champion': champ_df,
          'item': items_df,
          'game': matches_df,
          'summoner': summoner_df,
          'item_pick': item_picks_df,
          'game_item': match_items_df,
          'champ_select': champ_select_df,
          'game_instance': match_instance_df,
          'game_champ': game_champs_df
          }

# connecting to database
user = 'root'
password = 'root'
localhost = '127.0.0.1'
db_name = 'lol_dashboard'

engine = create_engine(f'mysql+mysqldb://{user}:{password}@{localhost}/{db_name}?charset=utf8')

# inserting fake values for regions
engine.execute('INSERT INTO League (ID, Region) '
               'VALUES (1, "North America"),'
               '(2, "Europe");'
               )

# loading in dataframes
for key in frames:
    frames[key].to_sql(con=engine, name=key, if_exists='append', index=False)
