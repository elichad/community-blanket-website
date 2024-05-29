from django.urls import path

from blankets.views import (
    BlanketCreate,
    BlanketDetail,
    BlanketUpdate,
    BlanketDelete,
    BlanketItemCreate,
    BlanketItemDetail,
    BlanketItemUpdate,
    BlanketItemDelete,
)

app_name = "blankets"
urlpatterns = [
    path("add/", BlanketCreate.as_view(), name="blanket-create"),
    path("<int:pk>/", BlanketDetail.as_view(), name="blanket-detail"),
    path("<int:pk>/edit", BlanketUpdate.as_view(), name="blanket-update"),
    path("<int:pk>/delete", BlanketDelete.as_view(), name="blanket-delete"),
    path("items/add/", BlanketItemCreate.as_view(), name="blanket-item-create"),
    path("items/<int:pk>/", BlanketItemDetail.as_view(), name="blanket-item-detail"),
    path(
        "items/<int:pk>/edit", BlanketItemUpdate.as_view(), name="blanket-item-update"
    ),
    path(
        "items/<int:pk>/delete", BlanketItemDelete.as_view(), name="blanket-item-delete"
    ),
]
