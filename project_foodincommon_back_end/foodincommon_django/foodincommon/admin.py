from django.contrib import admin

# Register your models here.
from .models import Restaurant, RestaurantList, Friendship

admin.site.register(Restaurant)
admin.site.register(RestaurantList)
admin.site.register(Friendship)
