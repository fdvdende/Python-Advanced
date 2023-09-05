import requests

API_KEY = 'd1526a9039658a6f76950cff21823aff'

city = 'soesterberg'

url = f'http://api.openweathermap.org/data/2.5/forecast/daily'\
       '?appid={API_KEY}'\
       '&units=metric'\
       '&mode=json'\
       '&q={city}'