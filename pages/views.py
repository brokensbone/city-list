from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def about_page_view(request):
    return HttpResponse("<h1>About us</h1>")

