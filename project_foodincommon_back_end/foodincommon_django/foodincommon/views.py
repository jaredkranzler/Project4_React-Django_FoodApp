from django.shortcuts import render, redirect

from .models import Restaurant, RestaurantList, Friendship
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RestaurantSerializer, RestaurantListSerializer, UserSerializer, UserSerializerWithToken
# from django.contrib.auth.decorators import login_required

# Create your views here.

# TODO finish views 08/16/2018

# Artist API List
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# Artist API Detail
class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# Song API List
class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all().prefetch_related('artist')
    serializer_class = SongSerializer

# Song API Detail
class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all().prefetch_related('artist')
    serializer_class = SongSerializer

# Artist API List
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# Artist API Detail
class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# Song API List
class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all().prefetch_related('artist')
    serializer_class = SongSerializer

# Song API Detail
class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all().prefetch_related('artist')
    serializer_class = SongSerializer
