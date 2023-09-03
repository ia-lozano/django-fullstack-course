from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

class IndexView(TemplateView):
    template_name="index.html"

class SchoolListView(ListView):
    # The ListView returns a context named after the model name: school_list
    # We can change the default context name object name:
    context_object_name = "schools"
    model = models.School

class SchoolDetailView(DetailView):
    # The DetailView returns a context named after the model: school_detail
    # We can change the default context object name:
    context_object_name = "school_detail"
    model = models.School
    template_name = 'cbv_app/school_detail.html'