from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from forms_app.forms import NewUser

# Create your views here.
def index(request):
    return render(request, "forms_app/index.html")

def form_page(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO something code
            print("VALIDATION SUCCESS!!")
            print(form.cleaned_data["name"])
            print(form.cleaned_data["email"])
            print(form.cleaned_data["text"])


    return render(request, "forms_app/form_page.html", {"form":form})

def signup(request):
    
    form_model = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error: Form invalid")

    return render(request, "forms_app/model_form.html", {"form_model": form_model})
