from django.contrib.auth.models import User
from django.db import models
from album.models import Album

class Track(models.Model):
    name = models.TextField(max_length= 100)
    number = models.IntegerField()
    id_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    gener = models.TextField(max_length= 100)
    composer = models.TextField(max_length= 100)
    url = models.URLField()
    time = models.DateTimeField()
    year = models.IntegerField()
    counter_likes = models.IntegerField()
    state = models.BooleanField(default= True)

class Track_likes(models.Model):
    id_user = models.ForeignKey(User,on_delete= models.CASCADE)
    id_song = models.ForeignKey(Track, on_delete= models.CASCADE)
