from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'events_needs/events_needs.html')

