# Weather Dashboard

A Django web app that shows real-time weather for multiple cities using the OpenWeatherMap API.

## Features
- User registration and login
- Track weather for multiple cities
- Detailed weather info (temperature, humidity, wind, pressure)
- Save favorite cities
- Switch between Fahrenheit and Celsius
- Edit user profile

## Setup

1. Install dependencies:
   pip install django requests

2. Run migrations:
   python manage.py migrate

3. Start the server:
   python manage.py runserver

4. Open browser:
   http://127.0.0.1:8000/

## Project Structure

**weatherproject/** - Django project settings
**weatherapp/** - Main application
  - models.py - Database models
  - views.py - Page logic
  - templates/ - HTML files
  - static/ - CSS, JS, images

## Usage

1. Register a new account
2. Login with your credentials
3. View weather dashboard
4. Add cities in Preferences
5. Click any city for detailed weather
6. Edit profile information

## Requirements
- Python 3.11+
- Django 5.1.3
- OpenWeatherMap API key

## Test Account
Username: testuser
Password: TestPass123!
