from django.shortcuts import render
from django.views import generic as views


class AddKidView(views.CreateView):
    pass


class DetailsKidView(views.DetailView):
    pass


class EditKidView(views.UpdateView):
    pass


class DeleteKidView(views.DeleteView):
    pass
