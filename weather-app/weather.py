from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()

def get_current_weather(city="Moscow") :
    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__" :
    city = input("Enter a city: ")

    if not bool(city.strip()):
        city = "Moscow"

    pprint(get_current_weather(city))
