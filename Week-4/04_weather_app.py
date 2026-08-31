"""Week 4 Practice 4: Weather App using OpenWeather API."""

import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url, timeout=10)
    data = response.json()
    if response.status_code == 200:
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Error:", data.get("message", "Unable to fetch weather."))


if __name__ == "__main__":
    get_weather(input("Enter city name: "))
