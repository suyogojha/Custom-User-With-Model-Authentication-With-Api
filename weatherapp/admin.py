from django.contrib import admin
from weatherapp.models import Weather, WeatherType, AppUser

# Register your models here.
class AdminWeather(admin.ModelAdmin):
    list_display = ('address', 'description')

admin.site.register(Weather, AdminWeather)
admin.site.register(WeatherType)
admin.site.register(AppUser)