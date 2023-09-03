from django.urls import path
from cbv_app import views

app_name="cbv_app"

urlpatterns =[
    path("", views.SchoolListView.as_view(), name="list"),
    path("<int:pk>", views.SchoolDetailView.as_view(), name="detail"),
]