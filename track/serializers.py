from rest_framework import serializers
from .models import Track
from album.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    id_album = AlbumSerializer(read_only = True)
    class Meta:
        model = Track
        fields = ("id", "name", "number","gener",
                    "composer", "url", "time", "year","counter_likes",
                    "state", "id_album")