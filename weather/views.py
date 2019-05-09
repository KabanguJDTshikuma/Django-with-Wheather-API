from django.shortcuts import render
import requests
from .models import City
from .forms import Cityform

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=59d3837fc29b30a6d855b7e795d5e98b'
    
    if request.method == 'POST':
        form = Cityform(request.POST) 
        form.save()

    form = Cityform()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': r['name'],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    #print(weather_data)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)
 