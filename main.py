
import requests, csv, json
import configparser

parser = configparser.ConfigParser()
parser.read('config.txt')


# Project plan
# - get data from  api
# add to some spreadsheet for activity simple task
# use pd for some manipulation
# add all to git

    

api = parser.get('API', 'access_key')
url = f"https://api.aviationstack.com/v1/flights?access_key={api}"

querystring = {"date":"2025-01-03"}

response = requests.get(url, params=querystring)
jsonObj = json.loads(response.text)
results = jsonObj['data']

print(results)
# for i in response:
#     print(i)

# filename = "aviation_data.csv"
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerows(rows)

