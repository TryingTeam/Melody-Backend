from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    """ Se define que modelo y campos se van a usar """
    class Meta:
        model = Album
        fields = '__all__'