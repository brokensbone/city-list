
from django.views.generic import ListView, DetailView
from .models import Business

class BusinessListView(ListView):
    model = Business
    template_name = 'places/business_list.html'
    context_object_name = 'businesses'
    queryset = Business.objects.order_by('name')

class BusinessDetailView(DetailView):
    model = Business
    template_name = 'places/business_detail.html'
    context_object_name = 'business'
