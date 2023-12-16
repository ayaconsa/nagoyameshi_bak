from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    explanation = models.CharField(max_length=200)