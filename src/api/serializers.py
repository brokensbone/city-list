from os import wait
from rest_framework import serializers
from places.models import Business, BusinessGroup, ImportedPlace, Location


class BusinessGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessGroup
        fields = ["name"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["latitude", "longitude", "address"]


class BusinessSerializer(serializers.ModelSerializer):
    business_group = BusinessGroupSerializer()
    location = LocationSerializer()

    class Meta:
        model = Business
        fields = [
            "id",
            "name",
            "business_group",
            "location",
            "category",
            "date_opened",
            "date_closed",
            "notes",
        ]


class ImportedPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportedPlace
        fields = ["latitude", "longitude", "name", "amenity"]
