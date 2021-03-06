from django import forms

from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoForm
        fields = ['title','image','description']