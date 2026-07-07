import numpy as np

from django.db import models
from django.urls import reverse

from planets.models import Planet

# Create your models here.


class SolarSystem(models.Model):
    """Model for tracking solar system projects."""

    name = models.CharField(max_length=256)
    creator = models.CharField(max_length=256)
    description = models.TextField()
    num_cols = models.IntegerField()
    num_rows = models.IntegerField()

    def get_absolute_url(self):
        return reverse("solar_systems:solar-system-detail", kwargs={"pk": self.pk})

    def get_solar_system_items(self):
        # loop over rows and columns and get all items where they exist
        items = np.empty((self.num_rows, self.num_cols), dtype=Planet)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                try:
                    item = SolarSystemItem.objects.get(
                        solar_system=self, row=row, column=col
                    )
                    planet = item.planet
                    items[row, col] = planet
                except SolarSystemItem.DoesNotExist:
                    continue
        return items

    def __str__(self):
        return self.name


class SolarSystemItem(models.Model):
    """Model to connect Planets and SolarSystems."""

    solar_system = models.ForeignKey(SolarSystem, on_delete=models.CASCADE)
    planet = models.ForeignKey(Planet, on_delete=models.PROTECT)
    column = models.PositiveIntegerField()
    row = models.PositiveIntegerField()

    class Meta:
        constraints = [
            # Planet can only be in one location
            models.UniqueConstraint("planet", name="unique_planet"),
            # Each solar_system cell can only contain one planet
            models.UniqueConstraint(
                "solar_system", "column", "row", name="unique_solar_system_column_row"
            ),
        ]

    def clean_column(self):
        if self.column >= self.solar_system.num_cols:
            raise ValueError("Column number exceeds number of columns in solar_system")

    def clean_row(self):
        if self.row >= self.solar_system.num_rows:
            raise ValueError("Row number exceeds number of rows in solar_system")

    def clean_fields(self, exclude=None):
        super().clean_fields()

        self.clean_column()
        self.clean_row()

    def __str__(self):
        return f"{self.solar_system.name} ({self.column}, {self.row})"

    def get_absolute_url(self):
        return reverse("solar_systems:solar-system-item-detail", kwargs={"pk": self.pk})
