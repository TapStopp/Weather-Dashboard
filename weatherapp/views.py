from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import UserProfile, WeatherPreference, WeatherData
from .forms import UserRegistrationForm, UserProfileForm, WeatherPreferenceForm
from .weather_service import get_weather_data, get_weather_icon_url, format_temperature

def splash_view(request):
    """Splash screen view"""
    return render(request, 'weatherapp/splash.html')

def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Update last access
                if hasattr(user, 'profile'):
                    user.profile.save()  # This triggers auto_now update
                messages.success(request, f'Welcome back, {user.first_name}!')
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'weatherapp/login.html', {'form': form})

@login_required
def logout_view(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('splash')

def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Weather App!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'weatherapp/registration.html', {'form': form})

@login_required
def home_view(request):
    """Main dashboard view with weather data"""
    # Get user's weather preferences
    preferences = WeatherPreference.objects.filter(user=request.user)
    
    # If user has no preferences, show default city
    if not preferences.exists():
        # Create a default preference for Poughkeepsie
        WeatherPreference.objects.create(
            user=request.user,
            city_name='Poughkeepsie',
            country_code='US',
            temperature_unit='imperial',
            is_favorite=True
        )
        preferences = WeatherPreference.objects.filter(user=request.user)
    
    # Fetch weather data for all preferred cities
    weather_list = []
    for pref in preferences:
        weather_data = get_weather_data(pref.city_name, pref.temperature_unit)
        if weather_data:
            weather_data['preference_id'] = pref.id
            weather_data['icon_url'] = get_weather_icon_url(weather_data['weather_icon'])
            weather_data['temp_formatted'] = format_temperature(
                weather_data['temperature'], 
                weather_data['units']
            )
            weather_list.append(weather_data)
    
    context = {
        'weather_list': weather_list,
        'user': request.user
    }
    return render(request, 'weatherapp/home.html', context)

@login_required
def weather_detail_view(request, city_name):
    """Detailed weather view for a specific city"""
    # Get the preference for this city
    try:
        preference = WeatherPreference.objects.get(user=request.user, city_name=city_name)
        units = preference.temperature_unit
    except WeatherPreference.DoesNotExist:
        units = 'imperial'
    
    # Fetch detailed weather data
    weather_data = get_weather_data(city_name, units)
    
    if not weather_data:
        messages.error(request, f'Could not fetch weather data for {city_name}')
        return redirect('home')
    
    weather_data['icon_url'] = get_weather_icon_url(weather_data['weather_icon'])
    weather_data['temp_formatted'] = format_temperature(weather_data['temperature'], units)
    weather_data['feels_like_formatted'] = format_temperature(weather_data['feels_like'], units)
    weather_data['temp_min_formatted'] = format_temperature(weather_data['temp_min'], units)
    weather_data['temp_max_formatted'] = format_temperature(weather_data['temp_max'], units)
    
    context = {
        'weather': weather_data,
        'city_name': city_name
    }
    return render(request, 'weatherapp/weather_detail.html', context)

@login_required
def profile_view(request):
    """User profile view and edit"""
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=profile)
    
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'weatherapp/profile.html', context)

@login_required
def preferences_view(request):
    """Manage weather preferences"""
    preferences = WeatherPreference.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = WeatherPreferenceForm(request.POST)
        if form.is_valid():
            preference = form.save(commit=False)
            preference.user = request.user
            try:
                preference.save()
                messages.success(request, f'Added {preference.city_name} to your preferences!')
            except:
                messages.error(request, f'{preference.city_name} is already in your preferences.')
            return redirect('preferences')
    else:
        form = WeatherPreferenceForm()
    
    context = {
        'preferences': preferences,
        'form': form
    }
    return render(request, 'weatherapp/preferences.html', context)

@login_required
@require_http_methods(["POST"])
def delete_preference_view(request, preference_id):
    """Delete a weather preference"""
    preference = get_object_or_404(WeatherPreference, id=preference_id, user=request.user)
    city_name = preference.city_name
    preference.delete()
    messages.success(request, f'Removed {city_name} from your preferences.')
    return redirect('preferences')

@login_required
def api_weather_view(request):
    """API endpoint to fetch weather data (for AJAX requests)"""
    city_name = request.GET.get('city', 'Poughkeepsie')
    units = request.GET.get('units', 'imperial')
    
    weather_data = get_weather_data(city_name, units)
    
    if weather_data:
        weather_data['icon_url'] = get_weather_icon_url(weather_data['weather_icon'])
        weather_data['temp_formatted'] = format_temperature(weather_data['temperature'], units)
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'Could not fetch weather data'}, status=400)
