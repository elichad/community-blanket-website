from typing import Collection
from django.db import models
from django.urls import reverse

from contributors.models import Person, get_anonymous_user


class Square(models.Model):
    """Model for tracking individual contributions."""

    name = models.CharField(max_length=256, help_text="A name for the square.")
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    creator = models.CharField(
        max_length=256,
        help_text='Your name, or a pseudonym. This will be displayed publicly - if you\'d rather not include any name at all, write "Anon".',
    )
    date_created = models.DateField(
        help_text="Enter the date when you finished the square, not including adding it to the blanket."
    )
    date_time_uploaded = models.DateTimeField(auto_now_add=True)
    description = models.CharField(
        max_length=1000,
        verbose_name="alt_text",
        help_text='A concise visual description of your square. For example, "red and yellow striped square".',
    )
    notes = models.TextField(
        blank=True,
        help_text="Anything you'd like others to know about the square - for example, why you chose the design, or what the colours mean.",
    )

    # TODO: fields relating to location in a larger blanket

    def get_absolute_url(self):
        return reverse("squares:square-detail", kwargs={"pk": self.pk})

    def clean_fields(self, exclude: Collection[str] | None = None) -> None:
        if not hasattr(self, "creator") and "creator" not in exclude:
            self.creator = get_anonymous_user()
        return super().clean_fields(exclude)

    def __str__(self):
        return f"#{self.id} {self.name} by {self.creator}"
