import requests
from django.conf import settings
from .models import WeatherData

# OpenWeatherMap API configuration
import os
API_KEY = os.environ.get('OPENWEATHER_API_KEY', '')
OPENWEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city_name, units='imperial'):
    """
    Fetch weather data from OpenWeatherMap API
    
    Args:
        city_name: Name of the city
        units: 'imperial' for Fahrenheit, 'metric' for Celsius
    
    Returns:
        Dictionary with weather data or None if error
    """
    try:
        params = {
            'q': city_name,
            'appid': OPENWEATHER_API_KEY,
            'units': units
        }
        
        response = requests.get(OPENWEATHER_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Parse and structure the weather data
        weather_info = {
            'city_name': data['name'],
            'country_code': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max'],
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'weather_main': data['weather'][0]['main'],
            'weather_description': data['weather'][0]['description'],
            'weather_icon': data['weather'][0]['icon'],
            'wind_speed': data['wind']['speed'],
            'wind_deg': data['wind'].get('deg', 0),
            'clouds': data['clouds']['all'],
            'units': units
        }
        
        # Cache the data in database
        WeatherData.objects.create(**{k: v for k, v in weather_info.items() if k != 'units'})
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing weather data: {e}")
        return None

def get_weather_icon_url(icon_code):
    """Get the full URL for a weather icon"""
    return f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

def format_temperature(temp, units='imperial'):
    """Format temperature with appropriate unit symbol"""
    symbol = '°F' if units == 'imperial' else '°C'
    return f"{temp:.1f}{symbol}"
