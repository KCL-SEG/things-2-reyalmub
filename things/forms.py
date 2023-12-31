from django import forms
from .models import Thing


"""Forms of the project."""

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(), 'quantity': forms.NumberInput()}