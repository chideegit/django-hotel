from django import forms 
from .models import * 

class AddHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        exclude = ('user', )

class UpdateHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        exclude = ('user', )