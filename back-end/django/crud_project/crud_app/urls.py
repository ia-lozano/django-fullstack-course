from django.urls import path
from crud_app import views

app_name = "crud_app"

urlpatterns = [
    path("", views.ConsoleListview.as_view(), name="list"),
    path("<int:pk>", views.ConsoleDetailView.as_view(), name="detail"),
    path("create/", views.ConsoleCreateView.as_view(), name="create"),
    path("add_game/", views.GameCreateView.as_view(), name="add_game"),
    path("update/<pk>", views.ConsoleUpdateView.as_view(), name="update"),
    path("delete/<pk>", views.ConsoleDeleteView.as_view(), name="delete"),
]

