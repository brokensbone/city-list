from rest_framework import serializers
from places.models import Business, BusinessGroup

class BusinessGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessGroup
        fields = ['name']

class BusinessSerializer(serializers.ModelSerializer):
    business_group = BusinessGroupSerializer()

    class Meta:
        model = Business
        fields = [
            'id', 'name', 'business_group', 'category', 'latitude', 'longitude',
            'date_opened', 'date_closed', 'notes'
        ]
