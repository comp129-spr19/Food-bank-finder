import datetime
import unittest


from django.utils import (
	timezone
)
from django.test import (
	TestCase
)

from .models import (
	FoodBankEvent
)


#import the database
#Based on the assumptions that:
	#Food bank table has: food_bank_ID(PK), food_bank_name, food_bank_address
							#food_bank_number, food_bank_website, operating_hrs
	#Events table: food_bank_ID(FK), event_ID(PK), event_name, event_description
class FoodBankEventsTests(TestCase):

	def test_string_representation(self):
		foodbank = FoodBankEvent(food_bank_name = "Jillian's foodbank")
		self.assertEqual(foodbank.get_name(), foodbank.food_bank_name)


	def test_future_dated_polls(self):
		foodbank = FoodBankEvent.objects.create(food_bank_name = "Jillian's foodbank",
			food_bank_event = "Coat drive", food_bank_date = (datetime.datetime.now() + datetime.timedelta(days=1)),
			food_bank_description = "Bring us coats")
		self.assertGreater(foodbank.food_bank_date, datetime.datetime.now())


	def test_past_dated_polls(self):
		foodbank = FoodBankEvent.objects.create(food_bank_name = "Jillian's foodbank",
			food_bank_event = "Coat drive", food_bank_date = (datetime.datetime.now() + datetime.timedelta(days=-5)),
			food_bank_description = "Bring us coats")
		self.assertLess(foodbank.food_bank_date, datetime.datetime.now())

	#TODO: write a function that returns true if the event has not occured yet
# 	def test_future_event_published(self):
# 		time = timezone.now() + datetime.timedelta(days=30)
# 		future_event = Event(food_bank_ID = "112",
# 						  event_description = "Future event", event_date = time)
# 		self.assertEquals(future_event.isFutureEvent(), True)

# 		Event(food_bank_ID = "112",
# 						  event_description = "Future event", event_date = "09/10/1996")
# 		#self.assertEquals(1,1)

# 	#TODO: make sure webpage returns Event unavailable in the case of past event
# 	#TODO: double check access of server is corrects
#     def test_past_event(self):
#     	create_event(food_bank_ID = "112", event_description = 
#     									"Past event", event_date = "09/10/1996")
#     	response = self.client.get(reverse('database'))
#     	self.assertContains(response, "Event unavailable")

#     	create_event(food_bank_ID = "112", event_description = 
#     								  "Future Event", event_date = "04/12/2020")
#     	response = self.client.get(reverse('database'))

#     	self.assertContains(response, "Future Event")
#     	create_event(food_bank_ID = "112", event_description = 
#     										  "Future Event", event_date = "")
#     	event1 = FoodBankEvents()



#     def test_food_bank_with_event_found_in_food_bank(self):
#     	create_food_bank(food_bank_ID = "112", food_bank_name = "St. Mary's", 
#     		food_bank_address = "123 Stockton, CA 95211")
#     	create_event(food_bank_ID = "112", event_description = "Coat drive", 
#     		event_date = "09/12/2020")
#     	self.assertContains(food_bank_ID)
#     	create_event(food_bank_ID = "116", event_description = "Coat drive", 
#     		event_date = "09/12/2020")
#     	self.assertFalse(food_bank_ID)

#     #TODO: create check_null_string function
#     def test_if_event_has_description(self):
#     	create_event(food_bank_ID = "112", event_description = "Coat drive", 
#     		event_date = "09/12/2020")
#     	self.assertTrue(check_null_string(event_description))
#     	create_event(food_bank_ID = "112", event_description = "", 
#     		event_date = "09/12/2020")
#     	self.assertFalse(check_null_string(event_description))

#     #TODO: create is_valid_date function
#     def test_if_event_has_date(self):
#     	create_event(food_bank_ID = "112", event_description = "Coat drive", 
#     		event_date = "09/12/2020")
#     	self.assertTrue(is_valid_date(event_date))
#     	create_event(food_bank_ID = "112", event_description = "Coat drive", 
#     		event_date = "ABBA")
#     	self.assertFalse(is_valid_date(event_date))
#     	create_event(food_bank_ID = "112", event_description = "Coat drive", 
#     		event_date = "")
#     	self.assertFalse(is_valid_date(event_date))

#     #TODO: create is_valid_address function
#     def test_food_bank_address(self):
#     	create_food_bank(food_bank_ID = "112", food_bank_name = "St. Mary's", 
#     		food_bank_address = "123 Stockton, CA 95211")
#     	self.assertTrue(is_valid_address(food_bank_address))
#     	create_food_bank(food_bank_ID = "112", food_bank_name = "St. Mary's", 
#     		food_bank_address = "")
#     	self.assertFalse(is_valid_address(food_bank_address))


# if __name__ == '__main__':
# 	unittest.main()