# here we will map our urls to view functions

from django.urls import path
from . import views


# we have here a url configuration module
urlpatterns = [
    path("hello/", views.say_hello)
]
