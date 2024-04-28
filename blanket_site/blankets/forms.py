from django.forms import ModelForm, fields

from blankets.models import Blanket, BlanketItem


class BlanketForm(ModelForm):
    class Meta:
        model = Blanket
        fields = ["name", "creator", "description", "num_cols", "num_rows"]


class BlanketItemForm(ModelForm):
    class Meta:
        model = BlanketItem
        fields = ["blanket", "square", "column", "row"]
