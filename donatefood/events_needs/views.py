from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>Testing donatefood/home/views.py</h1>")
    return render(request, 'events_needs/events_needs.html')
