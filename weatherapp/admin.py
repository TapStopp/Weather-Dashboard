from django.contrib import admin
from .models import UserProfile, WeatherPreference, WeatherData

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'created_on', 'last_access']
    search_fields = ['user__username', 'user__email']

@admin.register(WeatherPreference)
class WeatherPreferenceAdmin(admin.ModelAdmin):
    list_display = ['user', 'city_name', 'country_code', 'is_favorite', 'temperature_unit']
    list_filter = ['is_favorite', 'temperature_unit']
    search_fields = ['user__username', 'city_name']

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'country_code', 'temperature', 'weather_main', 'timestamp']
    list_filter = ['weather_main', 'timestamp']
    search_fields = ['city_name']
