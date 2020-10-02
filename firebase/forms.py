from django import forms
from django.forms import ModelForm
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(label='Enter a name')
    description = forms.CharField(label='Enter a description')
    image = forms.FileField(label='Select a image')

class ProductForm2(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']