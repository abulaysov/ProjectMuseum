from django.db import models


class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
