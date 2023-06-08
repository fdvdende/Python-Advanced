import json
import requests
from datetime import datetime
import logging

logging.basicConfig(
    filename = None, # or to a file 'example.log',
    level = logging.ERROR,
    format = '%(filename)s %(lineno)d %(asctime)s.%(msecs)03d - %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%S')

API_KEY = 'd1526a9039658a6f76950cff21823aff'

city = input('Geef een stad: ')

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?'
url += f'appid={API_KEY}&'
url += 'units=metric&'
url += 'mode=json&'
url += 'cnt=16&'
url += 'lang=nl&'
url += f'q={city}'

r = requests.get(url)

if r.status_code != 200:
    logging.error(f'HTTP error {r.status_code} - {r.reason} - {city}')

else:
    d = r.json()

    logging.debug(d)

    days = d['list']

    print(f'     datum      |   temp |    min |    max')
    for i, day in enumerate(days, 1):
        dt = datetime.fromtimestamp(day['dt'])
        temp = day['temp']['day']
        min = day['temp']['min']
        max = day['temp']['max']

        print(f'{i:2}   {dt.strftime("%d-%m-%Y")} | {temp:>5.1f}° | {min:>5.1f}° | {max:>5.1f}°')
