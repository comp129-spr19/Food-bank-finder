from django.contrib import admin
# this imports the models/tables we created 
# in order to show on the admin site
from .models import FoodBankEvents

# this line allows us to see the models 
# on the localhost admin site
admin.site.register(FoodBankEvents)