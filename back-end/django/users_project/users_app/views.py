from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from users_app.forms import UserForm, UserProfileInfoForm

## For login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, "users_app/index.html")

@login_required
def special(request):
    return HttpResponse("You're logged in!")

@login_required
def user_logout(request):
    print("logged in user has logged out")
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            ## Grabbing the user form and saving it into the DB.
            user = user_form.save()
            ## Hashing the password with the set_password method.
            user.set_password(user.password)
            ## Save hashed password to the DB.
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, "users_app/registration.html",
                  {"user_form": user_form, "profile_form": profile_form, "registered": registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print(username + " has loged in")
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
            
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid loggin details supplied")
    
    else:
        print("It seems that the user does not exists.... or something else went wrong")
        return render(request, "users_app/login.html", {})
