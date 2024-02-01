from django.urls import path

from squares.views import CreateSquare, UpdateSquare, DeleteSquare

urlpatterns = [
    path("add/", CreateSquare.as_view(), name="create-square"),
    path("<int:pk>/", UpdateSquare.as_view(), name="update-square"),
    path("<int:pk>/delete", DeleteSquare.as_view(), name="delete-square"),
]
