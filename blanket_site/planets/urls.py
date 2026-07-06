from django.urls import path

from planets.views import (
    all_planets,
    PlanetCreate,
    PlanetDetail,
    PlanetUpdate,
    PlanetDelete,
)

app_name = "planets"
urlpatterns = [
    path("", all_planets, name="all-planets"),
    path("add/", PlanetCreate.as_view(), name="planet-create"),
    path("<int:pk>/", PlanetDetail.as_view(), name="planet-detail"),
    path("<int:pk>/edit", PlanetUpdate.as_view(), name="planet-update"),
    path("<int:pk>/delete", PlanetDelete.as_view(), name="planet-delete"),
]
