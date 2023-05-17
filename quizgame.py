import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        if "weather" in weather_data and len(weather_data["weather"]) > 0:
            main_weather = weather_data["weather"][0].get("main")
            description = weather_data["weather"][0].get("description")
        else:
            print("Weather data not available.")
            return

        temperature = weather_data.get("main", {}).get("temp")
        humidity = weather_data.get("main", {}).get("humidity")
        wind_speed = weather_data.get("wind", {}).get("speed")

        print(f"Weather in {city}:")
        if main_weather:
            print(f"Main Weather: {main_weather}")
        if description:
            print(f"Description: {description}")
        if temperature:
            print(f"Temperature: {temperature}°C")
        if humidity:
            print(f"Humidity: {humidity}%")
        if wind_speed:
            print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or API error.")


# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
api_key = "51eb64e2014e322cf1d8f73d02db2f24"

city = input("Enter a city name: ")
get_weather(city, api_key)