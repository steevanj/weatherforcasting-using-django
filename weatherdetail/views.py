from django.shortcuts import render
import requests 
import datetime # assuming you're calling OpenWeatherMap API

def get_weather(city):
    api_key = '95b381f8db4fc6e00b746757b49349a9'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url).json()
    
    data = {
        'temp': response['main']['temp'],
        'city': city,
        'descriptions': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'day': datetime.date.today(),  
    }
    return data

def index(request):
    context = {}
    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            context = get_weather(city)

    return render(request, 'index.html', context)
