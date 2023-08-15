from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def landing(request):
    return HttpResponse("You're in the ProTwo landing page... i guess..")

def index(request):
    return HttpResponse("You're in the AppTwo/index page :)")

def help(request):
    context = {"template_tag": "Help Page"}
    return render(request, "AppTwo/help.html", context)

def users(request):
    user_list = User.objects.order_by("first_name")
    context = {"users": user_list}
    return render(request, "AppTwo/users.html",context)