import requests


from dotenv import load_dotenv
import os
import json
from models.model import Weather_model

load_dotenv()

URL = os.getenv('URL')
URL_OTHER = os.getenv('URL_OTHER')


def Weather(key: int) -> dict:
    response = requests.post(URL + f"{key}" + URL_OTHER)

    all_response = response.json()
    temp = all_response['main']['temp']
    feels_like = all_response['main']['feels_like']
    temp_min = all_response['main']['temp_min']
    temp_max = all_response['main']['temp_max']
    pressure = all_response['main']['pressure']
    humidity = all_response['main']['humidity']
    city = all_response['name']
    description = all_response['weather'][0]['description']

    w = Weather_model(temp, feels_like, temp_min, temp_max, pressure, humidity, city, description)

    return w








#https://api.openweathermap.org/data/2.5/weather?id=e718de38b0365585db9479332f71e3ec&appid={id_city}&units=metric&lang=ru