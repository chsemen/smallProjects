#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import json, requests, sys
import pprint
import csv

# outputFile = open('getOpenWeather_protected.csv', 'w', newline='')
# outputDictWriter = csv.DictWriter(outputFile, ['APPID'])
# outputDictWriter.writeheader()
# outputDictWriter.writerow({'APPID': '*'})
# outputFile.close()


exampleFile = open('getOpenWeather_protected.csv')
exampleDictReader = csv.DictReader(exampleFile)
APPID=''
for row in exampleDictReader:
    APPID=row['APPID']
    break




# if len(sys.argv) < 2:
#     print('Usage: getOpemWeather.py city_name, 2-letter_coutry_code')
#     sys.exit()
# location = ' '.join(sys.argv[1:])

location='Moscow RU'

# url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location,APPID)
url = f'https://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={APPID}'
print(url)
response = requests.get(url)
response.raise_for_status()
# pprint.pprint(response.text)
locationData = json.loads(response.text)
# pprint.pprint(locationData)
lat=locationData[0]['lat']
lon = locationData[0]['lon']

url =f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={APPID}'
print(url)

# print(response.text)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
# pprint.pprint(weatherData)
w=weatherData['list']
print(f'Current weather in {location}')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[8]['weather'][0]['main'], '-', w[8]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[16]['weather'][0]['main'], '-', w[16]['weather'][0]['description'])
