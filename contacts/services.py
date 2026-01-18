import requests


def get_coords(city_name):
    """
    Function returns latitude and longitude coordinates of provided city
    Accept: city name
    Return: tuple of coordinates
    """
    geo_url = (
        f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    )
    geo_response = requests.get(geo_url).json()

    if not geo_response:
        return None

    lat = geo_response[0]["lat"]
    lon = geo_response[0]["lon"]

    coords = (lat, lon)

    return coords


def get_weather(lat, lon):
    """
    Function returns weather data from given latitude and longitude coordinates
    Accept: latitude and longitude coordinates
    Return: weather data: temperature, humidity, wind speed
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url).json()

    current_data = response.get("current", {})

    weather = {
        "temp": current_data.get("temperature_2m", "-"),
        "humidity": current_data.get("relative_humidity_2m", "-"),
        "wind": current_data.get("wind_speed_10m", "-"),
    }
    return weather
