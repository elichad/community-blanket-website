from django.urls import path

from blankets.views import BlanketCreate, BlanketDetail, BlanketUpdate, BlanketDelete

app_name = "blankets"
urlpatterns = [
    path("add/", BlanketCreate.as_view(), name="blanket-create"),
    path("<int:pk>/", BlanketDetail.as_view(), name="blanket-detail"),
    path("<int:pk>/edit", BlanketUpdate.as_view(), name="blanket-update"),
    path("<int:pk>/delete", BlanketDelete.as_view(), name="blanket-delete"),
]
