from django.shortcuts import render
from django.urls import reverse_lazy

from solar_systems.models import SolarSystem, SolarSystemItem


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    emf_solar_system = None
    try:
        emf_solar_system = SolarSystem.objects.get(name="EMF Community Solar System")
        num_items = SolarSystemItem.objects.filter(
            solar_system=emf_solar_system
        ).count()
    except SolarSystem.DoesNotExist:
        num_items = None

    context = {"num_items": num_items, "object": emf_solar_system}

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
