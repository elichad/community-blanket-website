from django.urls import path

from squares.views import test

urlpatterns = [
    path("", test, name="test"),
]
