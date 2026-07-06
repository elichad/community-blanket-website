from django.contrib import admin
from planets.models import Planet


class PlanetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "creator", "date_time_uploaded")


admin.site.register(Planet, PlanetAdmin)
