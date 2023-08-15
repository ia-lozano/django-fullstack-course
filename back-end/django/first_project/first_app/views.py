from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

def index(request):
    # template = loader.get_template("first_app/index.html")
    context = {"insert_me": "Hello I'm from views.py!"}
    return render(request, "first_app/index.html", context)