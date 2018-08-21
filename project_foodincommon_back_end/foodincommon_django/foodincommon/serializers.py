from rest_framework import serializers
# from rest_framework_jwt.settings import api_settings
from .models import Restaurant, RestaurantList, Friendship
from django.contrib.auth.models import User


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'category', 'rating', 'longitude', 'latitude', 'api_res_id', 'city', 'state', 'zip', 'address', 'restaurant_lists')

class RestaurantListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantList
        fields = ('id', 'title', 'user_id', 'restaurant_id')

class FriendshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friendship
        fields = ('id', 'user_id1', 'user_id2')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'restaurant_lists', 'friendships')

# class UserSerializerWithToken(serializers.ModelSerializer):
#
#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only=True)
#
#     def get_token(self, obj):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#
#         payload = jwt_payload_handler(obj)
#         token = jwt_encode_handler(payload)
#         return token
#
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance
#
#     class Meta:
#         model = User
#         fields = ('token', 'username', 'password', 'restaurant_lists', 'friendship')
