from django.http import HttpResponse
from django.shortcuts import render
from places.models import Business


def home_page_view(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def about_page_view(request):
    return HttpResponse("<h1>About us</h1>")


def map_page_view(request):
    business = Business.objects.first()
    context = {
        'business': business
    }
    return render(request, 'pages/map.html', context)

