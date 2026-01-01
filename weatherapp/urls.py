from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash_view, name='splash'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('preferences/', views.preferences_view, name='preferences'),
    path('preferences/delete/<int:preference_id>/', views.delete_preference_view, name='delete_preference'),
    path('weather/<str:city_name>/', views.weather_detail_view, name='weather_detail'),
    path('api/weather/', views.api_weather_view, name='api_weather'),
]
