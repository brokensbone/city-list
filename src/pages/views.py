from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from places.models import Business, ImportedPlace
from .utils import (
    serialize_businesses_for_map,
    serialize_imported_places_for_map,
)


def home_page_view(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def about_page_view(request):
    return HttpResponse("<h1>About us</h1>")


def map_page_view(request):
    show_imports = request.GET.get("show_imports", False)

    context = {
        "lat": request.GET.get("lat", settings.MAP_CENTER_LAT),
        "lng": request.GET.get("lng", settings.MAP_CENTER_LNG),
        "zoom": request.GET.get("zoom", settings.MAP_ZOOM_LEVEL),
        "businesses": serialize_businesses_for_map(
            Business.objects.filter(date_closed__isnull=True)
        ),
        "imported_places": serialize_imported_places_for_map(
            ImportedPlace.objects.all() if show_imports else []
        ),
    }
    return render(request, "pages/map.html", context)

