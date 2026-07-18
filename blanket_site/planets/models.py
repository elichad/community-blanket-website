from typing import Collection
from django.db import models
from django.urls import reverse

from contributors.models import Person, get_anonymous_user
from common.models import ThumbnailGenerator
from solar_systems.models import SolarSystem, SolarSystemItem


class Planet(ThumbnailGenerator):
    """Model for tracking individual contributions."""

    name = models.CharField(max_length=256, help_text="A name for the planet.")
    image = models.ImageField(
        upload_to="uploads/planets/%Y/%m/%d/",
        help_text="A picture of the planet. Ensure the image is square (aspect ratio 1:1), and that the edges of the image are cropped as close as possible to the edge of the planet, without cutting off part of the planet.",
    )
    thumbnail = models.ImageField(
        upload_to="thumbnails/planets/",
        help_text="A thumbnail of the planet, generated automatically from the uploaded image.",
        null=True,
    )
    creator = models.CharField(
        max_length=256,
        help_text='Your name, or a pseudonym. This will be displayed publicly - if you\'d rather not include any name at all, write "Anon".',
        verbose_name="Discoverer",
    )
    date_created = models.DateField(
        help_text="Enter the date when you discovered (finished) the planet, not including adding it to the solar system. Format: YYYY-MM-DD",
        verbose_name="Date discovered",
    )
    date_time_uploaded = models.DateTimeField(auto_now_add=True)
    description = models.CharField(
        max_length=1000,
        verbose_name="Visual description",
        help_text='A concise visual description of the planet. For example, "red and yellow striped planet". This helps blind & low vision astronomers know what the planet looks like.',
    )
    notes = models.TextField(
        blank=True,
        help_text="Anything you'd like others to know about the planet - for example, how you made it, or if the colours mean something to you.",
    )

    # planet-specific bonus fields

    mass = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        help_text='The mass of your planet in <b>grams</b>. There are weighing scales in <a href="https://map.emfcamp.org/#18.5/52.04028161496325/-2.378171671045834/m=52.04028161496325,-2.378171671045834">Tekhnē-cal Village</a>. If you don\'t have weighing scales to hand, make a guess or enter 0.',
    )
    diameter = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        help_text='The diameter of your planet in <b>centimetres</b>. There are measuring tools in <a href="https://map.emfcamp.org/#18.5/52.04028161496325/-2.378171671045834/m=52.04028161496325,-2.378171671045834">Tekhnē-cal Village</a>. If you don\'t have measuring tools to hand, make a guess or enter 0.',
    )
    fun_fact = models.TextField(
        blank=True,
        help_text='A fun fact about your planet. For example, "the red spot is a giant storm", "the inhabitants are hackers", or "it\'s named after the discoverer\'s favourite Linux distro".',
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(mass__gte=0),
                name="mass_not_negative",
                violation_error_message="Mass cannot be negative.",
            ),
            models.CheckConstraint(
                check=models.Q(diameter__gte=0),
                name="diameter_not_negative",
                violation_error_message="Diameter cannot be negative.",
            ),
        ]

    def get_absolute_url(self):
        return reverse("planets:planet-detail", kwargs={"pk": self.pk})

    def clean_fields(self, exclude: Collection[str] | None = None) -> None:
        if not hasattr(self, "creator") and "creator" not in exclude:
            self.creator = get_anonymous_user()
        return super().clean_fields(exclude)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        print("adding planet to solar system...")

        try:
            emf_solar_system = SolarSystem.objects.get(
                name="EMF Community Solar System"
            )
            SolarSystemItem.objects.get_or_create(
                solar_system=emf_solar_system,
                planet=self,
                defaults={"distance": 0, "angle": 0},
            )
        except SolarSystem.DoesNotExist:
            pass

    def __str__(self):
        return f"#{self.id} {self.name} discovered by {self.creator}"
