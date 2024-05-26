from django.shortcuts import render
from django.urls import reverse_lazy

from blankets.models import Blanket, BlanketItem


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    try:
        emf_blanket = Blanket.objects.get(name="EMF Community Blanket")
        num_items = BlanketItem.objects.filter(blanket=emf_blanket).count()
    except Blanket.DoesNotExist:
        num_items = None

    context = {
        "num_items": num_items,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
