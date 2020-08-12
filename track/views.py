from rest_framework import generics
from .models import Track
from album.models import Album
from .serializers import TrackSerializer

class track_list(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class track_list_album(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = TrackSerializer

class track_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
