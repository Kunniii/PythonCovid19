from requests import get
import json
import os

def getJson():
	a = get('https://api.covid19api.com/total/country/viet-nam')
	return a.text

def formatJson(s):
	a = json.loads(s)
	a = a[-1]
	return a

def printInfo(jsonString):
	print()
	print("Country:       {}".format(jsonString['Country']))
	print("Confirmed day: {}".format(jsonString['Date']))
	print("Confirmed:     {}".format(jsonString['Confirmed']))
	print("Recovered:     {}".format(jsonString['Recovered']))
	print("Active:        {}".format(jsonString['Confirmed'] - jsonString['Recovered']))
	print("Deaths:        {}".format(jsonString['Deaths']))
	print()

printInfo(formatJson(getJson()))
os.system('pause')
	