from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import requests
from .forms import UserRegistrationForm, WeatherSearchForm
from .models import FavoriteLocation, SearchHistory
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Реєстрація успішна!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'weather/register.html', {'form': form})

def get_weather_data(city):
    api_key = settings.OPENWEATHER_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'uk'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        if response.status_code == 404:
            messages.error(request, 'Місто не знайдено. Перевірте правильність написання.')
        else:
            messages.error(request, 'Помилка при отриманні даних про погоду. Спробуйте пізніше.')
        return None

def home(request):
    weather_data = None
    if request.method == 'POST':
        form = WeatherSearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)
            
            if weather_data and request.user.is_authenticated:
                SearchHistory.objects.create(
                    user=request.user,
                    city=city,
                    country=weather_data['sys']['country'],
                    temperature=weather_data['main']['temp'],
                    description=weather_data['weather'][0]['description']
                )
    else:
        form = WeatherSearchForm()
    
    context = {
        'form': form,
        'weather_data': weather_data,
    }
    
    if request.user.is_authenticated:
        context['favorite_locations'] = FavoriteLocation.objects.filter(user=request.user)
        context['search_history'] = SearchHistory.objects.filter(user=request.user)[:5]
    
    return render(request, 'weather/home.html', context)

@login_required
def add_favorite(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        country = request.POST.get('country')
        
        if city and country:
            FavoriteLocation.objects.get_or_create(
                user=request.user,
                city=city,
                country=country
            )
            messages.success(request, 'Місце додано до улюблених!')
    
    return redirect('home')

@login_required
def remove_favorite(request, pk):
    try:
        favorite = FavoriteLocation.objects.get(pk=pk, user=request.user)
        favorite.delete()
        messages.success(request, 'Місце видалено з улюблених!')
    except FavoriteLocation.DoesNotExist:
        messages.error(request, 'Місце не знайдено!')
    
    return redirect('home')

@login_required
def profile(request):
    search_history = SearchHistory.objects.filter(user=request.user).order_by('-searched_at')[:10]
    favorite_locations = FavoriteLocation.objects.filter(user=request.user)
    
    context = {
        'search_history': search_history,
        'favorite_locations': favorite_locations,
    }
    
    return render(request, 'weather/profile.html', context)
