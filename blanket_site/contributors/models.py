from django.db import models


# Create your models here.
def get_anonymous_user():
    return Person.objects.get_or_create(name="Anonymous")[0]


class Person(models.Model):
    """Simple model for tracking creators"""

    name = models.CharField(max_length=256)
