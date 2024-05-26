from typing import Collection
from django.db import models
from django.urls import reverse

from contributors.models import Person, get_anonymous_user


class Square(models.Model):
    """Model for tracking individual contributions."""

    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    creator = models.CharField(max_length=256)
    date_created = models.DateField()
    date_time_uploaded = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    notes = models.TextField(blank=True)

    # TODO: fields relating to location in a larger blanket

    def get_absolute_url(self):
        return reverse("squares:square-detail", kwargs={"pk": self.pk})

    def clean_fields(self, exclude: Collection[str] | None = None) -> None:
        if not hasattr(self, "creator") and "creator" not in exclude:
            self.creator = get_anonymous_user()
        return super().clean_fields(exclude)

    def __str__(self):
        return f"#{self.id} {self.name} by {self.creator}"
