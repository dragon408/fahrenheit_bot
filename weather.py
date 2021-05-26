# import json # ONLY FOR DEBUGGING

import requests
import math
from datetime import datetime

def get_hourly_weather_forecast(lat, lon):
    res = requests.get("https://api.openweathermap.org/data/2.5/onecall",
                       params={'lat': lat, 'lon': lon, 'exclude': 'current,minutely,daily,alerts', 'units': 'metric', 'appid': '78ce81583979bfea2158bf3c06c076c9'})
    return res.json()

def parse_hourly_weather_forecast(data):
    hourly_forecast = data['hourly']

    temp = [0, 0, 0, 0]
    wind_speed = [0, 0, 0, 0]
    weather_by_hours = []

    for i in range(6, 30):
        forecast = hourly_forecast[i]
        daypart = math.floor(i / 6) - 1 # 0 is morning, 1 is day, 2 is evening, 3 is night,
        temp[daypart] += forecast['temp']
        wind_speed[daypart] += forecast['wind_speed']
        weather_by_hours.append(forecast['weather'][0]['id'])

    # get avarage temp, feels_like, wind_speed for night, morning, day and evening
    temp = list(map(lambda t: t / 6, temp))
    wind_speed = list(map(lambda t: t / 6, wind_speed))

    return [temp, wind_speed, weather_by_hours]

# FOR DEBUGGING
# with open("hourly_weather.json", "r") as hourly_weather:
#     data = json.load(hourly_weather)
#     print(parse_hourly_weather_forecast(data))

