from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy

from squares.models import Square
from squares.forms import SquareForm


class SquareDetail(DetailView):
    model = Square
    template_name = "square_detail.html"


class SquareCreate(CreateView):
    model = Square
    form_class = SquareForm
    template_name = "square_form.html"


class SquareUpdate(UpdateView):
    model = Square
    fields = ["name", "image", "creator", "date_created", "description", "notes"]

    # form_class = SquareForm


class SquareDelete(DeleteView):
    model = Square
    success_url = reverse_lazy("square-create")

    # form_class = SquareForm
