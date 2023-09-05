import requests

from datetime import datetime

city = 'soesterberg'

url =  'http://api.openweathermap.org/data/2.5/forecast/daily'\
       '?appid=d1526a9039658a6f76950cff21823aff'\
       '&cnt=14'\
       '&units=metric'\
       '&mode=json'\
      f'&q={city}'

response = requests.get(url)

if response.status_code == 200:
    d = response.json()
    print(d)

    for day in d['list']:
        timestamp = day['dt']
        dt = datetime.fromtimestamp(timestamp)
        temperature = day['temp']['day']

        print(f'{dt.strftime("%d-%m-%Y %A"):25} {temperature:.0f}°C.')

else:
    print('Error')
