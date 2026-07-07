from django.contrib import admin
from solar_systems.models import SolarSystem, SolarSystemItem


class SolarSystemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "num_cols", "num_rows")


class SolarSystemItemAdmin(admin.ModelAdmin):
    list_display = ("id", "planet", "solar_system", "column", "row")


admin.site.register(SolarSystem, SolarSystemAdmin)
admin.site.register(SolarSystemItem, SolarSystemItemAdmin)
