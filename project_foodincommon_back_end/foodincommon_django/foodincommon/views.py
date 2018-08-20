from django.shortcuts import render, redirect

from .models import Restaurant, RestaurantList
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RestaurantSerializer, RestaurantListSerializer, UserSerializer, UserSerializerWithToken
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

# # Artist API List
# class FriendshipList(generics.ListCreateAPIView):
#     queryset = Friendship.objects.all()
#     serializer_class = FriendshipSerializer
#
# # Artist API Detail
# class FriendshipDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Friendship.objects.all()
#     serializer_class = FriendshipSerializer
