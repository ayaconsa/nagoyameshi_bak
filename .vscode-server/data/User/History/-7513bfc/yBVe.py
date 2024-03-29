from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=20, default='')
    catch_copy = models.CharField(max_length=30, default='')
    explanation = models.CharField(max_length=200, default='')
    price_min = models.PositiveIntegerField(default='0')
    price_max = models.PositiveIntegerField(default='0')
    address = models.CharField(max_length=200, default='')
    tel = models.CharField(max_length=11, default='')
    open_time = models.CharField(max_length=5, default='')
    close_time = models.CharField(max_length=5, default='')
    close_day = models.CharField(max_length=5, default='')
    img = models.ImageField(blank=True, default="img/noImage.png")

class User(models.Model):
    USERNAME_FIELD = "username"
    username = models.CharField(max_length=50, default='')
    password1 = models.CharField(max_length=20, default='')
    password2 = models.CharField(max_length=20, default='')

