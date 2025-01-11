import configparser
import requests, csv, json
import pandas as pd
   
parser = configparser.ConfigParser()
parser.read('config.txt')
   
    # Get data from api
def api_call():
    api = parser.get('API', 'access_key')
    url = f"https://api.aviationstack.com/v1/flights?access_key={api}"

    querystring = {"date":"2025-01-03"}

    response = requests.get(url, params=querystring)
    jsonObj = json.loads(response.text)
    results = jsonObj['data']
    return results


    # load data in csv using pandas
def info_to_csv(results):
    myvar = pd.DataFrame(results)
    myvar.to_csv('aviation_data.csv')
    print(myvar)
