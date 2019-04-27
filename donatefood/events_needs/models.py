# this is import is needed/necessary for any table to be created
from django.db import models
from django.conf import settings
# django.utils.timezone

# Table is created here.
# The name of the clss is the name of the respective table
# Since this is an instance of Model we use model.Model
# Within the table created are the fields of our table

class FoodBankEvent(models.Model):
    food_bank_name = models.CharField(max_length=100, default = 'Food Bank Name')
    food_bank_event = models.CharField(max_length=100)
    food_bank_date = models.DateTimeField('Event Date')
    food_bank_description = models.TextField(blank=True)

    def __str__(self):
        return self.food_bank_name + ' ' + self.food_bank_event + ' ' + \
            str(self.food_bank_date) + ' ' + self.food_bank_description
