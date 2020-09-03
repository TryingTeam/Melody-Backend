from django.db import models

class Album(models.Model):
    name = models.TextField(max_length = 100)
    artists= models.TextField(max_length= 100)
    guest_artist= models.TextField(max_length= 100)
    year = models.IntegerField()
    image = models.TextField(max_length=100)
    state = models.BooleanField(default=True)

    def __str__(self):
        """ Return name album. """
        return self.name

