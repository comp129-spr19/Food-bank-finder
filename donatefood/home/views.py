from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("<h1>Testing donatefood/home/views.py</h1>")
    return render(request, 'home/home.html')
