""" Users models """

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """ Profile model.
    Proxy model that extends the base data with other information.
    """
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    gender = models.CharField(
        max_length = 50,
        blank = True
    )

    birthdate = models.DateField(blank = False)

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        """ Return username. """
        return self.user.username
