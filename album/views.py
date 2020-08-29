from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Album
from track.models import Track
from .serializers import AlbumSerializer
from track.serializers import TrackSerializer


class album_list(generics.ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    authentication_class = (TokenAuthentication)
    

class album_detail(generics.ListAPIView):
    serializer_class = TrackSerializer
    
    def get_queryset(self):
        album = self.request.query_params.get('pk')
        queryset = Track.objects.filter(id_album_id=album)

        return queryset
    
    #authentication_class = (TokenAuthentication)

    #queryset = Track.objects.all()
    #serializer_class = TrackSerializer

