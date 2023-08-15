from django.shortcuts import render
from django.http import HttpResponse
from models_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    context = {"access_records": webpages_list}
    return render(request, "models_app/index.html", context)