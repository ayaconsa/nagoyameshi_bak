from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    explanation = models.CharField(max_length=200)

class User(models.Model):
    USERNAME_FIELD = "username"
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
