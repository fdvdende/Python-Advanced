from datetime import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)

def get_weather_forecast(city):
    # openwheathermap api
    url = "http://api.openweathermap.org/data/2.5/forecast"
    url += "?appid=d1526a9039658a6f76950cff21823aff"
    url += "&units=metric"
    url += "&mode=json"
    url += "&lang=nl"
    url += "&q=" + city

    # print(url)

    try:
        response = requests.get(url)

    except Exception as err:
        print("Cannot connect to " + url)
        print(err)

    else:
        if (response.status_code == 200):
            decoded = response.json()
            return decoded

        elif response.status_code == 404:
            print("%s not found" % (city))

        else:
            print("error for city %s" % (city))


@app.route("/")
def index():
    s = '<h1 style="color:#880000;">Get the weather</h1>'
    s += '<a href="weather_forecast">hier</a>'
    return s

@app.route("/weather_forecast")
def question():
    city = 'Delft'

    weather_forecast = get_weather_forecast(city)

    content = {"city": city, "weather_forecast": []}
    for single_weather_forcast in weather_forecast['list']:
        d = {'dd': datetime.fromtimestamp(single_weather_forcast['dt']).strftime('%d-%m-%Y %H:%M'),
             'temp': single_weather_forcast['main']['temp'],
             'feels_like': single_weather_forcast['main']['feels_like'],
             'description': single_weather_forcast['weather'][0]['description'],
             }
        content["weather_forecast"].append(d)

    return render_template('weather_forecast.html', content = content)


app.run()