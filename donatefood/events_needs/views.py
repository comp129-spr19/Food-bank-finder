from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
		TemplateView, 
		ListView
)
from .models import FoodBankEvents



def index(request):
    # return HttpResponse("<h1>Testing donatefood/home/views.py</h1>")
    return render(request, 'events_needs/events_needs.html')

class EventView(TemplateView):
	template_name = 'events_needs/events_needs.html'

	def get(self, request):
		return FoodBankEvents.objects.all()