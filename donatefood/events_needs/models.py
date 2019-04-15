#this is import is needed/necessary for any table to be created
from django.db import models 

# Table is created here.
# The name of the clss is the name of the respective table
# Since this is an instance of Model we use model.Model
# Within the table created are the fields of our table
class FoodBanks(models.Model):
    food_bank_name = models.CharField(max_length = 100)
    food_bank_event = models.CharField(max_length = 100)
    food_bank_description = models.CharField(max_length= 500)
