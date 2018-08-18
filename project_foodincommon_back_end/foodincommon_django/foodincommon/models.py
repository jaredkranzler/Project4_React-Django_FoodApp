from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    api_res_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RestaurantList(models.Model):
    title = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurant_lists')
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_lists')

    def __str__(self):
        return self.title

class Friendship(models.Model):
    user_id1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship')
    user_id2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship')
