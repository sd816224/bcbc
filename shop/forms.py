from django import forms
from django.forms import ModelForm
from django.contrib import admin
from .models import Item,Item_images



class Item_imagesForm(ModelForm):
    images=forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "multiple":True}))
    class Meta:
        model=Item_images
        fields={'images',}


class ItemForm(ModelForm):
    class Meta:
        model=Item
        fields={'title','thumbnail','description','price'}
        labels={
            'title':'name of the item',
            'thumbnail':' ',
            'description':'description',
            'price':'price',
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'thumbnail':forms.FileInput(attrs={'class':'form-control'}),
            # 'description':forms.TextInput(attrs={'class':'form-control',}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
        }
