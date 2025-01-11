
import csv
from functions import api_call, info_to_csv
import pandas as pd



api_data = api_call()

update_csv = info_to_csv(api_data)

# open data from csv using pd

df = pd.read_csv('aviation_data.csv')

print(df) 