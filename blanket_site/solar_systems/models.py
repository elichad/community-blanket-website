import numpy as np

from django.db import models
from django.urls import reverse

# Create your models here.


class SolarSystem(models.Model):
    """Model for tracking solar system projects."""

    name = models.CharField(max_length=256)
    creator = models.CharField(max_length=256)
    description = models.TextField()
    max_distance = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        help_text="The maximum size of the solar system in <b>centimetres</b>.",
    )

    def get_absolute_url(self):
        return reverse("solar_systems:solar-system-detail", kwargs={"pk": self.pk})

    def get_solar_system_items(self):
        # get all items sorted by distance
        try:
            items = SolarSystemItem.objects.filter(solar_system=self).order_by(
                "distance", "angle"
            )
        except SolarSystemItem.DoesNotExist:
            return []
        return items

    def __str__(self):
        return self.name


class SolarSystemItem(models.Model):
    """Model to connect Planets and SolarSystems."""

    solar_system = models.ForeignKey(SolarSystem, on_delete=models.CASCADE)
    planet = models.ForeignKey("planets.Planet", on_delete=models.PROTECT)
    # distance from centre of system (r)
    distance = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        help_text="The distance in <b>centimetres</b> between the planet and the centre of the solar system.",
    )
    # angle round orbit (theta)
    angle = models.PositiveIntegerField(
        help_text="The number of <b>degrees</b> the planet has proceeded anticlockwise round its orbit."
    )

    class Meta:
        constraints = [
            # Planet can only be in one system
            models.UniqueConstraint("planet", name="unique_planet"),
            # Planets may not share a position
            models.UniqueConstraint(
                "solar_system", "distance", "angle", name="unique_solar_system_coords"
            ),
            models.CheckConstraint(
                check=models.Q(distance__gte=0),
                name="distance_not_negative",
                violation_error_message="Distance cannot be negative.",
            ),
            models.CheckConstraint(
                check=models.Q(angle__lt=360),
                name="angle_within_circle",
                violation_error_message="Angle cannot be more than 360 degrees.",
            ),
        ]

    def clean_distance(self):
        if self.distance >= self.solar_system.max_distance:
            raise ValueError("Distance exceeds maximum size of solar system")

    def clean_fields(self, exclude=None):
        super().clean_fields()

        self.clean_distance()

    def __str__(self):
        return f"{self.solar_system.name} ({self.distance}, {self.angle})"

    def get_absolute_url(self):
        return reverse("solar_systems:solar-system-item-detail", kwargs={"pk": self.pk})
