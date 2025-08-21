from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.utils import timezone
from places.models import Business, ImportedPlace
from .serializers import BusinessSerializer, ImportedPlaceSerializer


class StatusAPIView(APIView):
    """
    A simple endpoint to check the status of the API.
    """

    def get(self, request, *args, **kwargs):
        return Response({"status": "ok", "timestamp": timezone.now()})


class BusinessListAPIView(generics.ListAPIView):
    """
    An endpoint to list all open businesses.
    """

    queryset = Business.objects.filter(date_closed__isnull=True)
    serializer_class = BusinessSerializer


class ImportedPlacesListAPIView(generics.ListAPIView):
    queryset = ImportedPlace.objects.all()
    serializer_class = ImportedPlaceSerializer

