from django.forms import ModelForm, fields

from planets.models import Planet
from contributors.models import Person


class PlanetForm(ModelForm):
    class Meta:
        model = Planet
        fields = [
            "name",
            "image",
            "creator",
            "date_created",
            "mass",
            "diameter",
            "fun_fact",
            "description",
            "notes",
        ]
