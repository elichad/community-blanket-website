from typing import Collection
from django.db import models
from django.urls import reverse

from contributors.models import Person, get_anonymous_user
from common.models import ThumbnailGenerator


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
    )
    date_created = models.DateField(
        help_text="Enter the date when you finished the planet, not including adding it to the blanket. Format: YYYY-MM-DD"
    )
    date_time_uploaded = models.DateTimeField(auto_now_add=True)
    description = models.CharField(
        max_length=1000,
        verbose_name="Alt text",
        help_text='A concise visual description of your planet. For example, "red and yellow striped planet".',
    )
    notes = models.TextField(
        blank=True,
        help_text="Anything you'd like others to know about the planet - for example, why you chose the design, or what the colours mean.",
    )

    def get_absolute_url(self):
        return reverse("planets:planet-detail", kwargs={"pk": self.pk})

    def clean_fields(self, exclude: Collection[str] | None = None) -> None:
        if not hasattr(self, "creator") and "creator" not in exclude:
            self.creator = get_anonymous_user()
        return super().clean_fields(exclude)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"#{self.id} {self.name} discovered by {self.creator}"
