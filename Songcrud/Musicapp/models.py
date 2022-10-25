from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.
class Artiste(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE, primary_key=True)
    content = models.CharField(max_length=4000)
    song_title = models.CharField(max_length=100)

    def __str__(self):
        return self.song_title
    