# importing
import json
import requests
import time


# function that matches missing values in parent entities and child entities
def id_match(parent_df: object, parent_column, child_df, child_columns):
    for child_column in child_columns:

        # transforming parent column into a set for comparison
        parent_column_set = set(parent_df[parent_column])

        # removing duplicates for comparison
        child_column_set = set(child_df[child_column])

        # missing values present in the child entity but not parent entities
        differences = list(child_column_set - parent_column_set)

        if len(differences) != 0:

            # appending missing ids and updating parent entity for next iteration
            for difference in differences:
                parent_df = parent_df.append({f'{parent_column}': difference}, ignore_index=True)

    return parent_df


# function that calls riot api using requests and saves it to json
def api_extract(extract_type, key):
    path = 'D:/Python/lol_dashboard'

    if extract_type == 'summoner':

        # strings to put into url
        url_part_a = 'summoner'
        url_part_b = 'summoners'

        with open(path + '/data/summoners.json') as f:
            ids = json.load(f)

    elif extract_type == 'match':

        # strings to put into url
        url_part_a = 'match'
        url_part_b = 'matches'

        with open(path + '/data/match_listna1.json') as f:
            ids = json.load(f)

    counter = 0
    output = []

    for id_ in ids:
        try:
            request_url = f'https://na1.api.riotgames.com/lol/{url_part_a}/v4/{url_part_b}/{id_}?api_key={key}'
            response = requests.get(request_url)
            entity = response.json()
            output.append(entity)
        except:
            continue

        counter += 1
        print(counter)

        time.sleep(1.21)

    # saving for transform step
    with open(path + f'/data/loaded_{url_part_b}.json', 'w') as w:
        json.dump(output, w)

    return
