from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Track
from album.models import Album
from .serializers import TrackSerializer

class track_list(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class track_list_album(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = TrackSerializer

class track_detail(APIView):
    
    def get(self, request, pk):
        tracks =  Track.objects.all().filter(id_album = pk)
        serializer = TrackSerializer(tracks, many = True)
        return Response(serializer.data)
