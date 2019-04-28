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
