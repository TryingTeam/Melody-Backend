""" Tracks urls """
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from track import views

urlpatterns = [
    path(
        route = '',
        view = views.track_list.as_view(),
        name = 'tracks',
    ),
    path(
        route = '<int:pk>',
        view = views.track_detail.as_view(),
        name = 'track',
    ),
]
urlpatterns = format_suffix_patterns(urlpatterns)
