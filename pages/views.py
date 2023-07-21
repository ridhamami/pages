from django.shortcuts import render
from .models import GetInTouch
from .forms import FormGet
from django.http import HttpRequest
# Create your views here.

def index (request):
    if request.method == "POST":
        add_get = FormGet(request.POST)
        if add_get.is_valid():
            add_get.save()
    contex = {
        'form':FormGet(),
    }
   

    return render (request , 'pages/index.html',contex)
    

def contact (request):
    return render(request , 'pages/contact.html')

def about(request):
    return render(request,'pages/about.html')