from django.contrib import admin
# this imports the models/tables we created 
# in order to show on the admin site
from .models import FoodBanks, FoodBankEvents

# this line allows us to see the models 
# on the localhost admin site
admin.site.register(FoodBanks)
admin.site.register(FoodBankEvents)