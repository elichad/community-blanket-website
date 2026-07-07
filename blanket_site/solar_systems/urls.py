from django.urls import path

from solar_systems.views import (
    SolarSystemCreate,
    SolarSystemDetail,
    SolarSystemUpdate,
    SolarSystemDelete,
    SolarSystemItemCreate,
    SolarSystemItemDetail,
    SolarSystemItemUpdate,
    SolarSystemItemDelete,
)

app_name = "solar_systems"
urlpatterns = [
    path("add/", SolarSystemCreate.as_view(), name="solar-system-create"),
    path("<int:pk>/", SolarSystemDetail.as_view(), name="solar-system-detail"),
    path("<int:pk>/edit", SolarSystemUpdate.as_view(), name="solar-system-update"),
    path("<int:pk>/delete", SolarSystemDelete.as_view(), name="solar-system-delete"),
    path(
        "items/add/", SolarSystemItemCreate.as_view(), name="solar-system-item-create"
    ),
    path(
        "items/<int:pk>/",
        SolarSystemItemDetail.as_view(),
        name="solar-system-item-detail",
    ),
    path(
        "items/<int:pk>/edit",
        SolarSystemItemUpdate.as_view(),
        name="solar-system-item-update",
    ),
    path(
        "items/<int:pk>/delete",
        SolarSystemItemDelete.as_view(),
        name="solar-system-item-delete",
    ),
]
