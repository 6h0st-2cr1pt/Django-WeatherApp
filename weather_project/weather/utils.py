import requests
from datetime import datetime

def get_weather_data(city):
    api_key = '91f607409966c29f4f4191f97ee5ed19'  # Replace with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M'),
            'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M'),
        }
        return weather_data
    else:
        return None