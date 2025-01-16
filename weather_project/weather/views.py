from django.shortcuts import render
from .utils import get_weather_data

def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather_data(city)
        if weather_data:
            return render(request, 'weather/weather.html', {'weather': weather_data})
        else:
            error_message = "City not found. Please try again."
            return render(request, 'weather/weather.html', {'error': error_message})
    return render(request, 'weather/weather.html')