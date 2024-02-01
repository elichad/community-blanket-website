from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from squares.models import Square
from squares.forms import SquareForm


def test(request):
    return HttpResponse("Hello, world.")


class CreateSquare(CreateView):
    model = Square
    form_class = SquareForm
    template_name = "squares/square_form.html"


class UpdateSquare(UpdateView):
    model = Square
    fields = ["name", "image", "creator", "date_created", "description", "notes"]

    # form_class = SquareForm


class DeleteSquare(DeleteView):
    model = Square
    success_url = reverse_lazy("create-square")

    # form_class = SquareForm
