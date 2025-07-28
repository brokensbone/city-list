from django import forms

class MapPickerWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(attrs={'readonly': 'readonly'}),
            forms.TextInput(attrs={'readonly': 'readonly'}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.latitude, value.longitude]
        return [None, None]

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['subwidgets'][0]['attrs']['id'] = f'id_{name}_0'
        context['widget']['subwidgets'][1]['attrs']['id'] = f'id_{name}_1'
        return context
