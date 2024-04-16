from django import forms
from .models import Grossary

class GrossaryForm(forms.ModelForm):
    class Meta:
        model = Grossary
        fields = '__all__'
    