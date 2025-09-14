from django import forms
from .models import Business, Location


class LocationForm(forms.ModelForm):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Location
        fields = ["latitude", "longitude", "address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["address"].widget.attrs.update({"id": "id_address"})


class BusinessFromImportForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            "name",
            "business_group",
            "category",
            "date_opened",
            "notes",
        ]
