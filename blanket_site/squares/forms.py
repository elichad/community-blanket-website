from django.forms import ModelForm, fields

from squares.models import Square
from contributors.models import Person


class SquareForm(ModelForm):
    creator = fields.CharField(max_length=256)

    class Meta:
        model = Square
        fields = ["name", "image", "creator", "date_created", "description", "notes"]

    def clean_creator(self):
        """Find an existing Person in database with matching name, or create a new Person"""
        creator = self.cleaned_data["creator"]
        person, _ = Person.objects.get_or_create(name=creator)

        return person
