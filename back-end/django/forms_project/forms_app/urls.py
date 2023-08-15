from django.urls import path
from forms_app import views

urlpatterns = [
    path("", views.form_page, name="form_page"),
    path("signup/", views.signup, name="signup"),
]
