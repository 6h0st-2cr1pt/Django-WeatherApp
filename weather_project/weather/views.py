import requests
from django.shortcuts import render
from django.conf import settings
from datetime import datetime

def get_weather_data(city):
    api_key = "91f607409966c29f4f4191f97ee5ed19"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': round(data['main']['temp'], 1),
                'feels_like': round(data['main']['feels_like'], 1),
                'temp_min': round(data['main']['temp_min'], 1),
                'temp_max': round(data['main']['temp_max'], 1),
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'wind_deg': data['wind']['deg'],
                'wind_gust': data['wind'].get('gust', 'N/A'),
                'wind_direction': get_wind_direction(data['wind']['deg']),
                'clouds': data['clouds']['all'],
                'cloud_name': data['weather'][0]['description'],
                'visibility': data['visibility'],
                'precipitation': data.get('rain', {}).get('1h', 0),
                'precipitation_mode': 'rain' if 'rain' in data else 'no precipitation',
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
                'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S'),
                'lon': data['coord']['lon'],
                'lat': data['coord']['lat'],
                'timezone': f"UTC{'+' if data['timezone'] >= 0 else ''}{data['timezone'] // 3600:02d}:{data['timezone'] % 3600 // 60:02d}",
                'last_update': datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S'),
            }
            return weather_data
        else:
            return None
    except requests.RequestException:
        return None

def get_wind_direction(degrees):
    directions = ['North', 'North-Northeast', 'Northeast', 'East-Northeast', 'East', 'East-Southeast', 'Southeast', 'South-Southeast',
                  'South', 'South-Southwest', 'Southwest', 'West-Southwest', 'West', 'West-Northwest', 'Northwest', 'North-Northwest']
    index = round(degrees / (360. / len(directions))) % len(directions)
    return directions[index]

def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
    else:
        city = ''

    weather_data = get_weather_data(city)

    if weather_data:
        context = {
            'weather': weather_data,
        }
    else:
        context = {
            'error': 'Unable to fetch weather data. Please try again.'
        }

    return render(request, 'weather/weather.html', context)

