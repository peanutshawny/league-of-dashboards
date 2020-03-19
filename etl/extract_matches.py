# importing match list

from etl_functions import api_extract

# setting api key
key = 'RGAPI-83d9b69d-993f-48df-8bf6-0573100e4db0'

api_extract('match', key=key)


