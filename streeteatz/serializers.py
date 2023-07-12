from .models import Vendor
from .models import Item
from rest_framework import serializers

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'phone_number', 'location', 'address', 'status', 'hours', 'description', 'tags', 'website', 'img', 'wait_time', 'upvote', 'downvote', 'favorited', 'up_rating', 'down_rating', 'distanceFromUser']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'description', 'vendor']