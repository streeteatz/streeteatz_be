from .models import Vendor
from rest_framework import serializers

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'phone_number', 'location', 'address', 'status', 'hours', 'description', 'tags', 'website', 'img', 'wait_time', 'upvote', 'downvote', 'favorited', 'up_rating', 'down_rating', 'distanceFromUser']