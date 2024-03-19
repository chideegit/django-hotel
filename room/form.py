from django import forms 
from .models import * 

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'price']

class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'price']

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('user', 'is_available')

class UpdateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('user', 'is_available')

class AddBookRoomForm(forms.ModelForm):
    class Meta:
        model = BookRoom
        exclude = ('user', 'has_checked_out', 'room')

class UpdateBookRoomForm(forms.ModelForm):
    class Meta:
        model = BookRoom
        exclude = ('user', 'has_checked_out', 'room')