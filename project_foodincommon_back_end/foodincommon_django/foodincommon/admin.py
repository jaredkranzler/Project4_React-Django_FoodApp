from django.contrib import admin

# Register your models here.
from .models import Restaurant, RestaurantList

admin.site.register(Restaurant)
admin.site.register(RestaurantList)
