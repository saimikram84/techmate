import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CityForm

# Create your views here.


def get_weather(city):
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def index(request):
    weather_data = None
    data = {'form':CityForm}
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = 
    
    
    return render(request, 'weather/index.html',data)