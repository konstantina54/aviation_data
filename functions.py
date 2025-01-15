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
    # results = jsonObj['data']
    return jsonObj


    # load data in csv using pandas
def info_to_csv(api_results):
    results = api_results['data']
    myvar = pd.DataFrame(results)
    myvar.to_csv('aviation_data.csv')
    # print(myvar)

# results is a list

def arrival_delays():
#    df = pd.read_csv('aviation_data.csv')
# #    print(df) 
#    arrival_delay = df[['arrival']]
#    print(arrival_delay)
    count = 0
    delays_sum = 0
    with open('aviation_data.csv','r') as data:
        for line in csv.reader(data):
            for values in line:
            # values is a str
                # print(values)
                # print(values.find('{'))
                values = values.replace("'", '"')
                values = values.replace("None", "null")
                values = values.replace("False", "false")
                values = values.replace("True", "true")
            
                if values.find('{') == 0:
                    res = json.loads(values)
                    # print(res)
                    if 'baggage' in res.keys():
                        if res['delay'] != None:
                            count +=1
                            delays_sum += res['delay']
                            avarage_delay = (delays_sum/count)
                            print(count, delays_sum, avarage_delay)
                            return avarage_delay


