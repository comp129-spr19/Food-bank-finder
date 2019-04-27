from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodBankEvent

def index(request):
	return render(request, "events_needs/events_needs.html")

#TODO: Add this as separate page once database can pull data from form and be displayed
#def AddEvent(request):
#	return render (request, "AddEvent/add_event.html")

def add_event_form_submission(request):
	print("Form has been submitted") #printed on terminal
	fbname = request.POST["fbname"]
	ename = request.POST["ename"]
	date = request.POST.get("eventDate")
	descript = request.POST["descript"]

	food_bank_info = FoodBankEvent.objects.create(food_bank_name = fbname, food_bank_event = ename, 
									food_bank_date = date, food_bank_description = descript)
	

	food_bank_info.save()
	
	return render(request, "events_needs/events_needs.html")

