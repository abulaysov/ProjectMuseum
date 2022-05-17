from django.db import models


class Authors(models.Model):
    author_name = models.TextField()


class Genre(models.Model):
    genre_name = models.TextField()


class Pictures(models.Model):
    picture = models.ImageField(upload_to='pictures/')
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField(default='')
    annotations = models.CharField(max_length=50, default='')
    name_picture = models.CharField(default='', max_length=200)
    location = models.CharField(default='', max_length=200)
    
