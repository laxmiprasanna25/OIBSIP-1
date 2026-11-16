
import json
import urllib.request
import urllib.parse

def get_weather(city):
    try:
        # Find city coordinates
        city_url = "https://geocoding-api.open-meteo.com/v1/search?"
        city_params = urllib.parse.urlencode({
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        })

        request = urllib.request.Request(
            city_url + city_params,
            headers={"User-Agent": "PythonWeatherApp"}
        )

        with urllib.request.urlopen(request, timeout=15) as response:
            city_data = json.loads(response.read().decode())

        if not city_data.get("results"):
            print("City not found. Please try another city.")
            return

        location = city_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]

        # Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast?"
        weather_params = urllib.parse.urlencode({
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code"
        })

        request = urllib.request.Request(
            weather_url + weather_params,
            headers={"User-Agent": "PythonWeatherApp"}
        )

        with urllib.request.urlopen(request, timeout=15) as response:
            weather_data = json.loads(response.read().decode())

        current = weather_data["current"]

        print("\n========== WEATHER REPORT ==========")
        print("City:", location["name"])
        print("Country:", location.get("country", ""))
        print("Temperature:", current["temperature_2m"], "°C")
        print("Feels Like:", current["apparent_temperature"], "°C")
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Wind Speed:", current["wind_speed_10m"], "km/h")
        print("Weather:", get_condition(current["weather_code"]))
        print("===================================")

    except Exception as error:
        print("Unable to get weather:", error)


def get_condition(code):
    if code == 0:
        return "Clear Sky"
    elif code in [1, 2, 3]:
        return "Partly Cloudy"
    elif code in [45, 48]:
        return "Foggy"
    elif code in [51, 53, 55, 56, 57]:
        return "Drizzle"
    elif code in [61, 63, 65, 66, 67]:
        return "Rainy"
    elif code in [71, 73, 75, 77]:
        return "Snowy"
    elif code in [80, 81, 82]:
        return "Rain Showers"
    elif code in [95, 96, 99]:
        return "Thunderstorm"
    else:
        return "Unknown Weather"


def main():
    print("===== PYTHON WEATHER APP =====")

    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")


if __name__ == "__main__":
    main()
