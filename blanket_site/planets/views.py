from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render

from planets.models import Planet
from planets.forms import PlanetForm


def all_planets(request):
    """View function for home page of site."""

    planets = Planet.objects.all().order_by("pk")

    context = {"all_planets": planets}

    # Render the HTML template index.html with the data in the context variable
    return render(request, "all_planets.html", context=context)


class PlanetDetail(DetailView):
    model = Planet
    template_name = "planet_detail.html"


class PlanetCreate(CreateView):
    model = Planet
    form_class = PlanetForm
    template_name = "planet_form.html"


class PlanetUpdate(UpdateView):
    model = Planet
    fields = [
        "name",
        "image",
        "creator",
        "date_created",
        "mass",
        "diameter",
        "fun_fact",
        "description",
        "notes",
    ]

    # form_class = PlanetForm


class PlanetDelete(DeleteView):
    model = Planet
    success_url = reverse_lazy("planet-create")

    # form_class = PlanetForm
