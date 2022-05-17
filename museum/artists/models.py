from statistics import mode
from django.db import models


class Biographies(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    annotation = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    age = models.CharField(max_length=10)
    birth = models.CharField(max_length=50)
    death = models.CharField(max_length=50)
    height = models.CharField(max_length=5)
    family = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artists/')
    era = models.CharField(max_length=50, default='')
    genre = models.CharField(max_length=50, default='')