from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy

from solar_systems.models import SolarSystem, SolarSystemItem
from solar_systems.forms import SolarSystemForm, SolarSystemItemForm


class SolarSystemDetail(DetailView):
    model = SolarSystem
    template_name = "solar_system_detail.html"


class SolarSystemCreate(CreateView):
    model = SolarSystem
    form_class = SolarSystemForm
    template_name = "solar_system_form.html"


class SolarSystemUpdate(UpdateView):
    model = SolarSystem
    fields = ["name", "creator", "description"]

    # form_class = SolarSystemForm


class SolarSystemDelete(DeleteView):
    model = SolarSystem
    success_url = reverse_lazy("solar-system-create")

    # form_class = SolarSystemForm


class SolarSystemItemCreate(CreateView):
    model = SolarSystemItem
    form_class = SolarSystemItemForm
    template_name = "solar_system_item_form.html"


class SolarSystemItemDetail(DetailView):
    model = SolarSystemItem
    template_name = "solar_system_item_detail.html"


class SolarSystemItemUpdate(UpdateView):
    model = SolarSystemItem
    fields = ["name", "creator", "description"]

    # form_class = SolarSystemForm


class SolarSystemItemDelete(DeleteView):
    model = SolarSystemItem
    success_url = reverse_lazy("solar-system-detail")

    # form_class = SolarSystemForm
