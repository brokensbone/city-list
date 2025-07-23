from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('businesses/', views.BusinessListView.as_view(), name='business-list'),
    path('businesses/<int:pk>/', views.BusinessDetailView.as_view(), name='business-detail'),
]
