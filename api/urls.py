from django.urls import path
from .views import StatusAPIView, BusinessListAPIView

app_name = 'api'

urlpatterns = [
    path('status/', StatusAPIView.as_view(), name='status'),
    path('businesses/', BusinessListAPIView.as_view(), name='business-list'),
]
