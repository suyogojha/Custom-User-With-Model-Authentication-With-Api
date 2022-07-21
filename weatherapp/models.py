from datetime import datetime
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.
class AppUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=8)
    is_verified = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())
    update_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "app_user"
    
    def __str__(self):
        return self.email

class WeatherType(models.Model):
    weather_type = models.CharField(max_length=100)

    class Meta:
        db_table = "app_weather_type"
    
    def __str__(self):
        return self.weather_type

class Weather(models.Model):
    weather_type = models.ForeignKey(WeatherType, on_delete=models.CASCADE)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    updated_at = models.DateTimeField(default=0)

    class Meta:
        db_table = "app_weather"