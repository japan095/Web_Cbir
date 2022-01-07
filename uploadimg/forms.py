from django.forms import fields
from .models import Image
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']