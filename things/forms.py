from django import forms
from .models import Thing


"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        exclude = ['created_at']
    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}), 
        'quantity': forms.NumberInput(attrs={'min': 0, 'max': 100})
    }