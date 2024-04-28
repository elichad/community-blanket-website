from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy

from blankets.models import Blanket
from blankets.forms import BlanketForm


class BlanketDetail(DetailView):
    model = Blanket
    template_name = "blanket_detail.html"


class BlanketCreate(CreateView):
    model = Blanket
    form_class = BlanketForm
    template_name = "blanket_form.html"


class BlanketUpdate(UpdateView):
    model = Blanket
    fields = ["name", "creator", "description"]

    # form_class = BlanketForm


class BlanketDelete(DeleteView):
    model = Blanket
    success_url = reverse_lazy("blanket-create")

    # form_class = BlanketForm
