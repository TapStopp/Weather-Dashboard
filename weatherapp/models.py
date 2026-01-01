from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    """Extended user profile with additional information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.CharField(max_length=200, blank=True, default='default-avatar.png')
    created_on = models.DateTimeField(default=timezone.now)
    last_access = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class WeatherPreference(models.Model):
    """User's weather preferences and favorite cities"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weather_preferences')
    city_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10, blank=True)
    is_favorite = models.BooleanField(default=True)
    temperature_unit = models.CharField(
        max_length=10, 
        choices=[('imperial', 'Fahrenheit'), ('metric', 'Celsius')],
        default='imperial'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-is_favorite', 'city_name']
        unique_together = ['user', 'city_name']
    
    def __str__(self):
        return f"{self.user.username} - {self.city_name}"

class WeatherData(models.Model):
    """Cache for weather API data"""
    city_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    temperature = models.FloatField()
    feels_like = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    weather_main = models.CharField(max_length=50)
    weather_description = models.CharField(max_length=200)
    weather_icon = models.CharField(max_length=10)
    wind_speed = models.FloatField()
    wind_deg = models.IntegerField()
    clouds = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.city_name} - {self.weather_main} at {self.timestamp}"
