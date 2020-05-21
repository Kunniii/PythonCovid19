import requests
import json
import os

url = "https://covid-19-data.p.rapidapi.com/country"

querystring = {"format":"json","name":"vietnam"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "4b17149a46mshf7c1fead81eeb49p111d95jsndf394f34e4d9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

def printInfo(jsonString):
    print()
    print('Country:   {}'.format(jsonString['country']))
    print('Confirmed: {}'.format(jsonString['confirmed']))
    print('Recovered: {}'.format(jsonString['recovered']))
    print('Critical:  {}'.format(jsonString['critical']))
    print('Deaths:    {}'.format(jsonString['deaths']))
    print()
    print('Last update on: {}'.format(jsonString['lastUpdate'][:10]))
    print()

jsonString = json.loads(response.text)[0]

printInfo(jsonString)
os.system('pause')