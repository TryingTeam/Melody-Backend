""" Users urls """
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path(
        route = 'register',
        view = views.UserRegister.as_view(),
        name = 'register',
    ),
    path(
        route = 'login',
        view = views.Login.as_view(),
        name = 'login',
    ),
    path(
        route = 'logout',
        view = views.Logout.as_view(),
        name = 'logout',
    ),
]
urlpatterns = format_suffix_patterns(urlpatterns)
