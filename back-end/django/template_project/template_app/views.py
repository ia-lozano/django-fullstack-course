from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'text':'Hello World', 'number':1000 }
    return render(request, "template_app/index.html", context)

def other(request):
    return render(request, "template_app/other.html")

def relative(request):
    return render(request, "template_app/relative_url.html")