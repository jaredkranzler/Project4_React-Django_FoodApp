from django.urls import path
from . import views

urlpatterns = [
    path('api/user/', views.FriendshipListAPI.as_view(), name='user-list'),
    path('api/user/<int:pk>', views.FriendshipDetailAPI.as_view(), name='user-detail'),
    path('api/friendship/', views.FriendshipListAPI.as_view(), name='friendship-list'),
    path('api/friendship/<int:pk>', views.FriendshipDetailAPI.as_view(), name='friendship-detail'),
    path('api/restaurants/', views.RestaurantListAPI.as_view(), name='restaurant-list'),
    path('api/restaurants/<int:pk>', views.RestaurantDetailAPI.as_view(), name='restaurant-detail'),
    path('api/restaurant_lists/', views.RestaurantListListAPI.as_view(), name='restaurant-list-list'),
    path('api/restaurant_lists/<int:pk>', views.RestaurantListDetailAPI.as_view(), name='restaurant-list-detail'),
    path('api/yelp/businesses/<str:location_query>/<str:term_query>/<int:limit_query>', views.yelp_business_search, name='yelp_business_search'),
    path('api/yelp/businesses/<str:id_query>', views.yelp_business_detail, name='yelp_business_detail'),
    path('api/ip/', views.ip_address, name='ip_address'),
]
