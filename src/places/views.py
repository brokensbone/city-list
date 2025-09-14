
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from .forms import BusinessFromImportForm
from .models import Business, BusinessGroup, ImportedPlace, Location


class BusinessListView(ListView):
    model = Business
    template_name = "places/business_list.html"
    context_object_name = "businesses"
    queryset = Business.objects.order_by("name")


class BusinessDetailView(DetailView):
    model = Business
    template_name = "places/business_detail.html"
    context_object_name = "business"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["imported_place"] = ImportedPlace.objects.get(
                location=self.object.location
            )
        except ImportedPlace.DoesNotExist:
            context["imported_place"] = None
        return context



class BusinessGroupDetailView(DetailView):
    model = BusinessGroup
    template_name = "places/business_group_detail.html"
    context_object_name = "business_group"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["businesses"] = Business.objects.filter(
            business_group=self.object
        ).order_by("name")
        return context


def convert_imported_place(request, pk):
    imported_place = get_object_or_404(ImportedPlace, pk=pk)

    if request.method == "POST":
        form = BusinessFromImportForm(request.POST)
        if form.is_valid():
            # Create a new Location
            location = Location.objects.create(
                latitude=imported_place.latitude,
                longitude=imported_place.longitude,
            )

            # Create a new Business
            business = form.save(commit=False)
            business.location = location
            business.save()

            # Link the ImportedPlace to the new Location
            imported_place.location = location
            imported_place.save()

            return redirect("business_detail", pk=business.pk)
    else:
        form = BusinessFromImportForm(
            initial={
                "name": imported_place.name,
            }
        )

    context = {
        "form": form,
        "imported_place": imported_place,
    }
    return render(request, "places/convert_imported_place.html", context)
