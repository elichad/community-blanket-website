from django.urls import path

from squares.views import SquareCreate, SquareDetail, SquareUpdate, SquareDelete

app_name = "squares"
urlpatterns = [
    path("add/", SquareCreate.as_view(), name="square-create"),
    path("<int:pk>/", SquareDetail.as_view(), name="square-detail"),
    path("<int:pk>/edit", SquareUpdate.as_view(), name="square-update"),
    path("<int:pk>/delete", SquareDelete.as_view(), name="square-delete"),
]
