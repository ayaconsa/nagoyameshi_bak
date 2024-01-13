from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    catch_copy = models.CharField(max_length=30)
    explanation = models.CharField(max_length=200)
    price_min = models.PositiveIntegerField()
    price_max = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=11)
    open_time = models.CharField(max_length=5)
    close_time = models.CharField(max_length=5)
    close_day = models.CharField(max_length=5)
    img = models.ImageField(blank=True, default="img/noImage.png")

class User(models.Model):
    USERNAME_FIELD = "username"
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

