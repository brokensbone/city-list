from django import forms
from .models import Location
from .widgets import MapPickerWidget

class LocationForm(forms.ModelForm):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Location
        fields = ['latitude', 'longitude', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'id': 'id_address'})
