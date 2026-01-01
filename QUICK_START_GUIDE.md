# Weather App - Quick Start Guide

## 🚀 Get Started in 5 Minutes!

### Step 1: Extract the Project
```bash
unzip weather_final_project.zip
cd weather_final
```

### Step 2: Install Dependencies
```bash
pip install django requests
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Database
```bash
python manage.py migrate
```

### Step 4: Run the Server
```bash
python manage.py runserver
```

### Step 5: Open in Browser
Navigate to: **http://127.0.0.1:8000/**

---

## 🎯 First Time User Guide

### 1. Welcome Screen
- Press **SPACEBAR** to continue from the splash screen

### 2. Create an Account
- Click **"Register here"** on the login page
- Fill in all fields:
  - Username (unique)
  - First Name
  - Last Name
  - Email
  - Phone Number
  - Date of Birth
  - Password (and confirm)
- Click **Submit**

### 3. View Weather Dashboard
- After registration, you'll see the weather dashboard
- Default city: **Poughkeepsie, US** is automatically added
- Click on any city card to see detailed weather

### 4. Add More Cities
- Click **"Preferences"** in the navigation menu
- Enter city name (e.g., "New York")
- Enter country code (e.g., "US")
- Choose temperature unit (Fahrenheit or Celsius)
- Check "Mark as favorite" if desired
- Click **"Add City"**

### 5. Explore Features
- **Weather Details**: Click any city card for comprehensive weather info
- **Profile**: Edit your personal information
- **Preferences**: Manage your favorite cities
- **Logout**: End your session

---

## 🧪 Test Account (Already Created)

If you want to skip registration and test immediately:

- **Username**: `testuser`
- **Password**: `TestPass123!`

This account already has:
- ✅ Profile information filled
- ✅ Two cities added (New York, Poughkeepsie)
- ✅ Fahrenheit temperature unit

---

## 📋 Project Features Checklist

### Core Features
- ✅ User Registration & Authentication
- ✅ Real-time Weather Data (OpenWeatherMap API)
- ✅ Multi-city Weather Dashboard
- ✅ Detailed Weather View
- ✅ User Profile Management
- ✅ Weather Preferences (Favorite Cities)
- ✅ Temperature Unit Selection (F/C)
- ✅ Responsive Design

### Technical Features
- ✅ Django 5.1.3 Framework
- ✅ SQLite Database
- ✅ Custom User Models
- ✅ Form Validation
- ✅ CSRF Protection
- ✅ Session Authentication
- ✅ RESTful API Integration
- ✅ Template Inheritance

---

## 🗂️ Project Structure Overview

```
weather_final/
├── weatherproject/          # Django project settings
├── weatherapp/             # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Django forms
│   ├── weather_service.py  # API integration
│   ├── templates/          # HTML templates
│   └── static/             # CSS, JS, images
├── db.sqlite3              # SQLite database
├── manage.py               # Django management
├── README.md               # Full documentation
├── PROJECT_DOCUMENTATION.md # Technical docs
└── requirements.txt        # Dependencies
```

---

## 🔧 Common Commands

### Run Development Server
```bash
python manage.py runserver
```

### Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```
Then access admin at: http://127.0.0.1:8000/admin/

### Apply Database Migrations
```bash
python manage.py migrate
```

### Create New Migrations (after model changes)
```bash
python manage.py makemigrations
```

### Collect Static Files (for production)
```bash
python manage.py collectstatic
```

---

## 🌐 Available URLs

| URL | Description | Auth Required |
|-----|-------------|---------------|
| `/` | Splash screen | No |
| `/login/` | User login | No |
| `/register/` | User registration | No |
| `/home/` | Weather dashboard | Yes |
| `/weather/<city>/` | Weather details | Yes |
| `/profile/` | Edit profile | Yes |
| `/preferences/` | Manage cities | Yes |
| `/logout/` | Logout | Yes |
| `/admin/` | Admin interface | Superuser |

---

## 💡 Tips & Tricks

### Adding Cities
- Use proper city names (e.g., "New York" not "NYC")
- Country code is 2 letters (e.g., "US", "UK", "CA")
- Check spelling if weather doesn't load

### Temperature Units
- Fahrenheit: Used in USA
- Celsius: Used internationally
- Setting applies to all your cities

### Profile Information
- All fields are required
- Email must be valid format
- Phone can include dashes or spaces
- Date of birth uses date picker

### Weather Data
- Updates in real-time on each page load
- Includes current conditions only (not forecast)
- Shows temperature, humidity, wind, pressure, etc.
- Weather icons from OpenWeatherMap

---

## ❓ Troubleshooting

### Problem: "No module named django"
**Solution**: Install Django
```bash
pip install django
```

### Problem: "Table doesn't exist"
**Solution**: Run migrations
```bash
python manage.py migrate
```

### Problem: Weather not loading
**Solutions**:
1. Check internet connection
2. Verify city name spelling
3. Confirm country code is correct
4. Wait a moment and refresh

### Problem: Can't login
**Solutions**:
1. Verify username (not email)
2. Check password (case-sensitive)
3. Register if no account exists

### Problem: CSRF error on form submission
**Solution**: The project is configured correctly, but if you deploy to a different domain, add it to `CSRF_TRUSTED_ORIGINS` in `settings.py`

---

## 📚 Documentation Files

1. **README.md** - Comprehensive project documentation
2. **PROJECT_DOCUMENTATION.md** - Technical documentation
3. **QUICK_START_GUIDE.md** - This file!

---

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Django framework proficiency
- ✅ Database modeling and ORM
- ✅ User authentication systems
- ✅ RESTful API integration
- ✅ Form handling and validation
- ✅ Template rendering
- ✅ Static file management
- ✅ Security best practices
- ✅ Full-stack web development

---

## 🚀 Next Steps

After exploring the basic features:

1. **Admin Interface**: Create a superuser and explore Django admin
2. **Add More Cities**: Build your personal weather dashboard
3. **Customize**: Modify CSS to change the look and feel
4. **Extend**: Add new features like weather forecasts
5. **Deploy**: Host on a platform like Heroku or PythonAnywhere

---

## 📞 Support

For questions about the project:
- Check **README.md** for detailed documentation
- Review **PROJECT_DOCUMENTATION.md** for technical details
- Examine the code comments for inline explanations

---

## ✅ Verification Checklist

Before submitting, verify:
- [ ] Project runs without errors
- [ ] Can register a new user
- [ ] Can login and logout
- [ ] Weather dashboard displays correctly
- [ ] Can add and remove cities
- [ ] Can view weather details
- [ ] Can edit profile
- [ ] All forms validate properly
- [ ] Navigation works correctly
- [ ] Styling is consistent

---

**Happy Coding! 🌤️**

---

*Last Updated: December 2, 2025*
*Django Version: 5.1.3*
*Python Version: 3.11+*
