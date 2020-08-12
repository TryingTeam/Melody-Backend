""" Albums urls """
from django.urls import path
from album import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(
        route = '',
        view = views.album_list.as_view(),
        name = 'albums',
    ),
    path(
        route = '<int:pk>',
        view = views.album_detail.as_view(),
        name = 'album',
    ),
]
urlpatterns = format_suffix_patterns(urlpatterns)
