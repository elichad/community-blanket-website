from django.forms import ModelForm, fields

from solar_systems.models import SolarSystem, SolarSystemItem


class SolarSystemForm(ModelForm):
    class Meta:
        model = SolarSystem
        fields = ["name", "creator", "description", "max_distance"]


class SolarSystemItemForm(ModelForm):
    class Meta:
        model = SolarSystemItem
        fields = ["solar_system", "planet", "distance", "angle"]
