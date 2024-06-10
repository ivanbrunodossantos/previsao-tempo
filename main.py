import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "São Paulo"  # Substitua pela cidade desejada

url = f"http://api.openweathermap.org/data/2.5/weather?q={
    CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    print(f"Weather in {CITY}: {weather}")
    print(f"Temperature: {temperature}°C")
else:
    print("Failed to fetch weather data")
