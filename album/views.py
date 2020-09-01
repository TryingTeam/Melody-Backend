from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Album
from track.models import Track
from .serializers import AlbumSerializer
from track.serializers import TrackSerializer

class AlbumList(APIView):
    def get(self, request):
        albums =  Album.objects.all()
        serializer = AlbumSerializer(albums, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        new_album = AlbumSerializer(data=request.data)
        if new_album.is_valid():
            new_album.save()
            return Response(new_album.data, status=201)
        return Response(new_album.errors, status=404)
        


class AlbumDetail(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        album = self.get_object(pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)
     
    def put(self, request, pk):
        album = self.get_object(pk)
        edit_album = AlbumSerializer(album, data = request.data)
        if edit_album.is_valid():
            edit_album.save()
            return Response(edit_album.data)
        return Response(edit_album.errors, status=400)

    def delete(self, request, pk):
        album = self.get_object(pk)
        album.delete()
        return Response(status=204)