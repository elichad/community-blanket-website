from django.forms import ModelForm, fields

from blankets.models import Blanket


class BlanketForm(ModelForm):
    class Meta:
        model = Blanket
        fields = ["name", "creator", "description", "width", "height"]
