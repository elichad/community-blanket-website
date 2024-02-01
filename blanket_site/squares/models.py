from django.db import models

from contributors.models import Person, get_anonymous_user


class Square(models.Model):
    """Model for tracking individual contributions."""

    name = models.CharField(max_length=256)
    image = models.ImageField()
    creator = models.ForeignKey(Person, on_delete=models.SET(get_anonymous_user))
    date_created = models.DateField()
    date_uploaded = models.DateTimeField()
    description = models.TextField()
    notes = models.TextField(blank=True)

    # TODO: fields relating to location in a larger blanket
