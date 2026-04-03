from django.urls import path
from . import views

app_name = "places"

urlpatterns = [
    path("businesses/", views.BusinessListView.as_view(), name="business-list"),
    path(
        "businesses/<int:pk>/",
        views.BusinessDetailView.as_view(),
        name="business_detail",
    ),
    path(
        "business-groups/<int:pk>/",
        views.BusinessGroupDetailView.as_view(),
        name="business-group-detail",
    ),
    path(
        "imported-places/<int:pk>/convert/",
        views.convert_imported_place,
        name="convert_imported_place",
    ),
]
