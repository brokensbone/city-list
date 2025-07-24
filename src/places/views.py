
from django.views.generic import ListView, DetailView
from .models import Business, BusinessGroup

class BusinessListView(ListView):
    model = Business
    template_name = 'places/business_list.html'
    context_object_name = 'businesses'
    queryset = Business.objects.order_by('name')

class BusinessDetailView(DetailView):
    model = Business
    template_name = 'places/business_detail.html'
    context_object_name = 'business'

class BusinessGroupDetailView(DetailView):
    model = BusinessGroup
    template_name = 'places/business_group_detail.html'
    context_object_name = 'business_group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['businesses'] = Business.objects.filter(business_group=self.object).order_by('name')
        return context
