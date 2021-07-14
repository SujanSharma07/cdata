from django import forms
from .models import *


class RegForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Full Name"}))
    profession = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Profession"}))
    mobile = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': "Contact Number"}))

    class Meta:
        model = Registered
        fields = '__all__'
