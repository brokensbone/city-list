from rest_framework import serializers
from places.models import Business, BusinessGroup, Location

class BusinessGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessGroup
        fields = ['name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['latitude', 'longitude', 'address']

class BusinessSerializer(serializers.ModelSerializer):
    business_group = BusinessGroupSerializer()
    location = LocationSerializer()

    class Meta:
        model = Business
        fields = [
            'id', 'name', 'business_group', 'location', 'category',
            'date_opened', 'date_closed', 'notes'
        ]
