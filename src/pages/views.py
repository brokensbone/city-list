from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def home_page_view(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def about_page_view(request):
    return HttpResponse("<h1>About us</h1>")


def map_page_view(request):
    context = {
        'lat': request.GET.get('lat', settings.MAP_CENTER_LAT),
        'lng': request.GET.get('lng', settings.MAP_CENTER_LNG),
        'zoom': request.GET.get('zoom', settings.MAP_ZOOM_LEVEL),
    }
    return render(request, 'pages/map.html', context)

