from django.contrib import admin
from solar_systems.models import SolarSystem, SolarSystemItem


class SolarSystemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "max_distance")


class SolarSystemItemAdmin(admin.ModelAdmin):
    list_display = ("id", "planet", "solar_system", "distance", "angle")


admin.site.register(SolarSystem, SolarSystemAdmin)
admin.site.register(SolarSystemItem, SolarSystemItemAdmin)
