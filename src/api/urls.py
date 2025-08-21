from django.urls import path
from .views import ImportedPlacesListAPIView, StatusAPIView, BusinessListAPIView

app_name = "api"

urlpatterns = [
    path("status/", StatusAPIView.as_view(), name="status"),
    path("businesses/", BusinessListAPIView.as_view(), name="business-list"),
    path("imports/", ImportedPlacesListAPIView.as_view(), name="imported-places-list"),
]
