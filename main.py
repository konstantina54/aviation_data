
import csv
from functions import api_call, info_to_csv, arrival_delays
# import pandas as pd



api_data = api_call()

update_csv = info_to_csv(api_data)

delays = arrival_delays()
# calculate avarage delay time
# can calculate most common airport
# calculate how many manage to catch up the delay from departure to arrival

# df = pd.read_csv('aviation_data.csv')
# print(df) 
