from django.shortcuts import render, redirect
import requests
import json
from django.http import JsonResponse
from .models import Restaurant, RestaurantList, Friendship
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RestaurantSerializer, RestaurantListSerializer, UserSerializer, FriendshipSerializer
# from django.contrib.auth.decorators import login_required

# Create your views here.

# TODO finish views 08/16/2018

# Artist API List
class RestaurantListAPI(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# Artist API Detail
class RestaurantDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# Song API List
class RestaurantListListAPI(generics.ListCreateAPIView):
    queryset = RestaurantList.objects.all()
    serializer_class = RestaurantListSerializer

# Song API Detail
class RestaurantListDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantList.objects.all()
    serializer_class = RestaurantListSerializer

class FriendshipListAPI(generics.ListCreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

# Song API Detail
class FriendshipDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

class UserListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Song API Detail
class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def yelp_business_search(request, location_query, term_query, limit_query):
    client_id = 'a3x1b8b59MxxH8FUk_vCZNco6_UyvcCPxqBonIz6F7zKie57BtlRFFw7CORC0_BQiAgOeXytSl78DX8DXzvPPGwmWIpeHDYBG8DZjr_54Ln7jUnMOC_4Bcdl0LV1W3Yx'
    location = location_query
    term = term_query
    limit = limit_query
    url = 'https://api.yelp.com/v3/businesses/search?location={0}&term={1}&limit={2}'

    headers = {
        'Authorization': 'Bearer ' + client_id
    }

    r = requests.get(url.format(location, term, limit), headers=headers)
    rjson = r.json()

    restaurant_list = []

    for restaurant in rjson['businesses']:
        restaurant_list.append(restaurant)

    data = {
        'restaurant_list': restaurant_list
    }

    return JsonResponse(data)
# # Artist API List
# class FriendshipList(generics.ListCreateAPIView):
#     queryset = Friendship.objects.all()
#     serializer_class = FriendshipSerializer
#
# # Artist API Detail
# class FriendshipDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Friendship.objects.all()
#     serializer_class = FriendshipSerializer
