from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views.generic import (View, TemplateView, ListView, DetailView, 
                                  CreateView, UpdateView, DeleteView)

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class ConsoleListview(ListView):
    context_object_name = "consoles"
    model = models.Console

class ConsoleDetailView(DetailView):
    context_object_name = "console_detail"
    model = models.Console
    template_name = "crud_app/games.html"

class ConsoleCreateView(CreateView):
    # this view expects a template named console_form.html
    fields = ('name', 'brand', 'emulator')
    model = models.Console

class GameCreateView(CreateView):
    # this view expects a template named game_form.html
    fields = ('name', 'release_year', 'console')
    model = models.Game
    success_url = reverse_lazy("crud_app:list")

class ConsoleUpdateView(UpdateView):
    # Coma at the end seems to be mandatory
    fields = ('emulator',)
    model = models.Console

class ConsoleDeleteView(DeleteView):
    model = models.Console
    success_url = reverse_lazy("crud_app:list")