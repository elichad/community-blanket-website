from django.forms import ModelForm, fields

from solar_systems.models import SolarSystem, SolarSystemItem


class SolarSystemForm(ModelForm):
    class Meta:
        model = SolarSystem
        fields = ["name", "creator", "description", "num_cols", "num_rows"]


class SolarSystemItemForm(ModelForm):
    class Meta:
        model = SolarSystemItem
        fields = ["solar_system", "planet", "column", "row"]
