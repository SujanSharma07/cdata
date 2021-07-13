from django import forms
from .models import *


class RegForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2', 'placeholder': "Full Name"}))
    profession = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control m-2', 'placeholder': "Profession"}))
    mobile = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control m-2', 'placeholder': "Contact Number"}))

    class Meta:
        model = Registered
        fields = '__all__'
