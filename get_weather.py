import requests
from datetime import datetime

def get_weather_forecast(location=None, latitude=None, longitude=None):
    api_key = "API KEY"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"

    # Check if location is provided, if not, use latitude and longitude
    if location:
        # Use geocoding to get latitude and longitude
        geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}"
        geocode_response = requests.get(geocode_url).json()
        if geocode_response:
            latitude = geocode_response[0]['lat']
            longitude = geocode_response[0]['lon']
        else:
            print("Location not found.")
            return
    elif latitude is None or longitude is None:
        print("Please provide either a location name or both latitude and longitude.")
        return

    # Prepare the URL for fetching the weather data
    complete_url = f"{base_url}lat={latitude}&lon={longitude}&exclude=current,minutely,hourly,alerts&units=metric&appid={api_key}"

    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data.get('daily'):
        for i, day in enumerate(weather_data['daily'][:7]):
            date = datetime.fromtimestamp(day['dt']).strftime('%Y-%m-%d')
            temp_day = day['temp']['day']
            temp_night = day['temp']['night']
            description = day['weather'][0]['description']
            print(f"Date: {date}, Day: {temp_day}°C, Night: {temp_night}°C, Weather: {description}")
    else:
        print("Weather data not found.")

# Example usage:
# get_weather_forecast(location="George ")
# Or using latitude and longitude
get_weather_forecast(latitude=-33.960400, longitude=22.456240)


'''
icon url:
https://openweathermap.org/weather-conditions
https://openweathermap.org/img/wn/10d@2x.png
10d

{'dt': 1708682400, 
'sunrise': 1708661536, 
'sunset': 1708708521, 
'moonrise': 1708707780, 
'moonset': 1708656900, 
'moon_phase': 0.47, 
'temp': {'day': 20.45, 'min': 15.56, 'max': 23.15, 'night': 19.54, 'eve': 22.05, 'morn': 16.41}, 
'feels_like': {'day': 20.3, 'night': 19.77, 'eve': 22.19, 'morn': 16.12}, 
'pressure': 1010, 
'humidity': 67, 
'dew_point': 14.12, 
'wind_speed': 3.79, 
'wind_deg': 140, 
'wind_gust': 4.64, 
'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 
'clouds': 12, 
'pop': 0, 
'uvi': 11.84}
'''
