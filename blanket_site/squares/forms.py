from django.forms import ModelForm, fields

from squares.models import Square
from contributors.models import Person


class SquareForm(ModelForm):
    class Meta:
        model = Square
        fields = ["name", "image", "creator", "date_created", "description", "notes"]
