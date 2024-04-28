from django.db import models
from django.urls import reverse

from squares.models import Square

# Create your models here.


class Blanket(models.Model):
    """Model for tracking individual contributions."""

    name = models.CharField(max_length=256)
    creator = models.CharField(max_length=256)
    description = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()

    def get_absolute_url(self):
        return reverse("blankets:blanket-detail", kwargs={"pk": self.pk})


class BlanketItem(models.Model):
    """Model to connect Squares and Blankets."""

    blanket = models.ForeignKey(Blanket, on_delete=models.CASCADE)
    square = models.ForeignKey(Square, on_delete=models.PROTECT)
    location_x = models.IntegerField()
    location_y = models.IntegerField()
